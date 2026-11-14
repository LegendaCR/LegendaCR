#!/usr/bin/env python3
"""Render the neofetch-style profile card (dark_mode.svg / light_mode.svg).

Pulls live numbers from the GitHub REST API. Set GH_TOKEN to a personal access
token of the profile owner to include private repositories; without it (or with
the Actions GITHUB_TOKEN) only public repositories are counted.
"""
import datetime as dt
import html
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

USER = "LegendaCR"
ROOT = pathlib.Path(__file__).resolve().parent.parent
def load_art(name):
    return (ROOT / "scripts" / name).read_text().rstrip("\n").split("\n")


ART = {"light": load_art("ascii.txt"), "dark": load_art("ascii_dark.txt")}
UPTIME_SINCE = dt.date(2024, 4, 1)  # start of commercial development
WIDTH = 57  # characters in the info column
ART_FONT, ART_LH = 10, 12.3  # small glyphs = more detail in the portrait

INFO = [
    ("header", "ilya@legenda"),
    ("kv", "OS", "Arch Linux, Ubuntu Server"),
    ("kv", "Uptime", "{uptime}"),
    ("kv", "Host", "SPbPU · Software Engineering"),
    ("kv", "Kernel", "Fullstack Developer"),
    ("kv", "IDE", "VS Code, Cursor, Vim"),
    ("blank",),
    ("kv", "Languages.Programming", "TypeScript, JavaScript, SQL"),
    ("kv", "Languages.Computer", "HTML, CSS, JSON, YAML"),
    ("kv", "Languages.Real", "Russian, English"),
    ("blank",),
    ("kv", "Stack.Frontend", "React, Vite, Tailwind"),
    ("kv", "Stack.Backend", "Node.js, Express, PostgreSQL"),
    ("kv", "Stack.Telegram", "Bot API, Mini Apps, Stars"),
    ("kv", "Stack.DevOps", "Docker, nginx, PM2, Cloudflare"),
    ("kv", "Stack.AI", "Claude API, AI content autopilot"),
    ("section", "Contact"),
    ("kv", "Website", "legenda-store.ru"),
    ("kv", "Telegram", "@Legenda_CR"),
    ("kv", "Channel", "@legasu"),
    ("kv", "GitVerse", "LegendaCR"),
    ("section", "GitHub Stats"),
    ("stats_repos",),
    ("stats_commits",),
    ("stats_loc",),
]

PROJECTS = [
    ("Verdikt Base", [("Type", "Telegram Mini App"),
                      ("Stack", "TS · React · Express · PostgreSQL"),
                      ("Access", "initData → JWT, channel-gated"),
                      ("Link", "@verdikt_menu_bot")]),
    ("Attract Platform", [("Type", "Telegram SaaS, paid channels"),
                          ("Stack", "Node.js · Express · PostgreSQL"),
                          ("Core", "billing, plans, auto-kick"),
                          ("Link", "@attractsub_bot")]),
    ("Brain Train", [("Type", "Telegram Mini App, games"),
                     ("Stack", "TS · React · Vite · Express"),
                     ("Core", "Stars payments, anti-cheat"),
                     ("Link", "@braintrainru_bot")]),
    ("Safronic", [("Type", "Website + 2 Telegram bots"),
                  ("Stack", "React · Express · PostgreSQL"),
                  ("Core", "client dashboard, XLSX quotes"),
                  ("Link", "safronic.ru")]),
    ("AI News", [("Type", "AI-run Telegram news channel"),
                 ("Stack", "Claude API (Sonnet 5.5) · Bot API"),
                 ("Core", "finds news, writes, auto-posts"),
                 ("Link", "@AI_News_c")]),
    ("Legend Defense Bot", [("Type", "Anti-spam for groups"),
                            ("Stack", "Node.js · Telegram Bot API"),
                            ("Core", "filters, bypass-proof matching"),
                            ("Link", "@Legend_defense_bot")]),
]
MORE = "@all Bot, FunPay automation, CRM / CMS systems, websites"
COL_W = 46  # characters per project column

THEMES = {
    "dark": dict(bg="#161b22", border="#30363d", text="#c9d1d9", art="#f0f6fc", key="#ffa657",
                 value="#a5d6ff", muted="#616e7f", add="#3fb950", sub="#f85149"),
    "light": dict(bg="#f6f8fa", border="#d0d7de", text="#24292f", art="#24292f", key="#953800",
                  value="#0a3069", muted="#8c959f", add="#1a7f37", sub="#cf222e"),
}


# ---------------------------------------------------------------- GitHub data

def api(path, token):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-card",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, json.loads(r.read() or "null")
        except urllib.error.URLError as e:
            if isinstance(e, urllib.error.HTTPError) or attempt == 2:
                raise
            time.sleep(5)


def list_repos(token):
    """Owner's PAT -> all repos incl. private; anything else -> public only."""
    if token:
        try:
            _, me = api("/user", token)
            if me and me.get("login", "").lower() == USER.lower():
                path = "/user/repos?affiliation=owner,collaborator,organization_member&per_page=100&page={}"
            else:
                path = None
        except urllib.error.HTTPError:
            path = None
    else:
        path = None
    path = path or f"/users/{USER}/repos?type=all&per_page=100&page={{}}"
    repos, page = [], 1
    while True:
        _, batch = api(path.format(page), token)
        repos += batch
        if len(batch) < 100:
            return repos
        page += 1


def contributor_stats(full_name, token):
    """Commits / additions / deletions by USER in one repo (GitHub computes these lazily)."""
    for _ in range(8):
        status, data = api(f"/repos/{full_name}/stats/contributors", token)
        if status == 202 or data is None:
            time.sleep(4)
            continue
        for c in data or []:
            if (c.get("author") or {}).get("login", "").lower() == USER.lower():
                return (c["total"], sum(w["a"] for w in c["weeks"]), sum(w["d"] for w in c["weeks"]))
        return 0, 0, 0
    return 0, 0, 0


def collect(token):
    _, user = api(f"/users/{USER}", token)
    repos = [r for r in list_repos(token) if not r.get("fork")]
    owned = [r for r in repos if r["owner"]["login"].lower() == USER.lower()]
    commits = added = deleted = contributed = 0
    for r in repos:
        c, a, d = contributor_stats(r["full_name"], token)
        commits, added, deleted = commits + c, added + a, deleted + d
        contributed += c > 0
    return dict(repos=len(owned), contributed=contributed,
                stars=sum(r["stargazers_count"] for r in owned),
                followers=user["followers"], commits=commits,
                added=added, deleted=deleted, loc=added - deleted)


def uptime(since, today):
    y, m, d = today.year - since.year, today.month - since.month, today.day - since.day
    if d < 0:
        m -= 1
        prev = (today.replace(day=1) - dt.timedelta(days=1))
        d += prev.day
    if m < 0:
        y, m = y - 1, m + 12
    plural = lambda n, w: f"{n} {w}{'' if n == 1 else 's'}"
    return f"{plural(y, 'year')}, {plural(m, 'month')}, {plural(d, 'day')}"


# ---------------------------------------------------------------- rendering

def span(cls, s):
    return f'<tspan class="{cls}">{html.escape(s)}</tspan>'


def kv_line(key, value, width=WIDTH):
    """'. Key: ....... value' padded to a fixed width."""
    dots = max(1, width - len(key) - len(value) - 5)
    return (span("m", ". ") + span("k", key) + ":" + span("m", " " + "." * dots + " ")
            + span("v", value))


def two_col(k1, v1, k2, v2, left_w=32):
    """Two key/value pairs on one line, split at left_w characters."""
    d1 = max(1, left_w - len(k1) - len(v1) - 5)
    d2 = max(1, WIDTH - left_w - len(k2) - len(v2) - 5)
    return (span("m", ". ") + span("k", k1) + ":" + span("m", " " + "." * d1 + " ") + span("v", v1)
            + span("m", " | ") + span("k", k2) + ":" + span("m", " " + "." * d2 + " ") + span("v", v2))


def info_lines(s, today):
    out = []
    for item in INFO:
        kind = item[0]
        if kind == "header":
            out.append(item[1] + " " + span("m", "—" * (WIDTH - len(item[1]) - 1)))
        elif kind == "section":
            out.append(span("m", "- ") + item[1] + " " + span("m", "—" * (WIDTH - len(item[1]) - 3)))
        elif kind == "blank":
            out.append(span("m", "."))
        elif kind == "kv":
            out.append(kv_line(item[1], item[2].format(uptime=uptime(UPTIME_SINCE, today))))
        elif kind == "stats_repos":
            v1 = f"{s['repos']}"
            contrib = f" {{Contributed: {s['contributed']}}}"
            left = len("Repos") + len(v1) + len(contrib)
            d1 = max(1, 32 - left - 5)
            d2 = max(1, WIDTH - 32 - len("Stars") - len(str(s['stars'])) - 5)
            out.append(span("m", ". ") + span("k", "Repos") + ":" + span("m", " " + "." * d1 + " ")
                       + span("v", v1) + " {" + span("k", "Contributed") + ": " + span("v", str(s["contributed"]))
                       + "}" + span("m", " | ") + span("k", "Stars") + ":"
                       + span("m", " " + "." * d2 + " ") + span("v", str(s["stars"])))
        elif kind == "stats_commits":
            out.append(two_col("Commits", f"{s['commits']:,}", "Followers", f"{s['followers']:,}"))
        elif kind == "stats_loc":
            add, sub = f"{s['added']:,}++", f"{s['deleted']:,}--"
            tail = f" ( {add}, {sub} )"
            key, val = "Lines of Code on GitHub", f"{s['loc']:,}"
            dots = max(1, WIDTH - len(key) - len(val) - len(tail) - 5)
            out.append(span("m", ". ") + span("k", key) + ":" + span("m", " " + "." * dots + " ")
                       + span("v", val) + " ( " + span("add", add) + ", " + span("sub", sub) + " )")
    return out


def render(theme, stats, today):
    c = THEMES[theme]
    lh, top, info_x = 20, 30, 410
    info = info_lines(stats, today)
    art_top = top - 6
    height = max(top + (len(info) - 1) * lh, art_top + (len(ART[theme]) - 1) * ART_LH) + 22
    art = "\n".join(f'<tspan x="15" y="{art_top + i * ART_LH:.1f}">{html.escape(l)}</tspan>' for i, l in enumerate(ART[theme]))
    txt = "\n".join(f'<tspan x="{info_x}" y="{top + i * lh}">{l}</tspan>' for i, l in enumerate(info))
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,'JetBrains Mono','DejaVu Sans Mono',monospace" width="985px" height="{height}px" font-size="16px">
<style>
.k {{fill: {c["key"]};}}
.v {{fill: {c["value"]};}}
.m {{fill: {c["muted"]};}}
.add {{fill: {c["add"]};}}
.sub {{fill: {c["sub"]};}}
text, tspan {{white-space: pre; font-variant-ligatures: none;}}
</style>
<rect width="985px" height="{height}px" fill="{c["bg"]}" rx="15"/>
<text x="15" y="30" fill="{c["art"]}" class="ascii" font-size="{ART_FONT}px" xml:space="preserve">
{art}
</text>
<text x="{info_x}" y="30" fill="{c["text"]}" xml:space="preserve">
{txt}
</text>
</svg>
'''


def section(title, width):
    return span("m", "- ") + title + " " + span("m", "—" * (width - len(title) - 3))


def render_projects(theme):
    """Second card: featured projects in two columns, like `ls` output in the terminal."""
    c = THEMES[theme]
    lh, top, xs = 20, 30, (20, 510)
    lines = []  # (x, y_index, markup)
    lines.append((xs[0], 0, span("k", "ilya@legenda") + ":" + span("v", "~") + "$ ls ~/projects --featured"))
    row = 2
    for i in range(0, len(PROJECTS), 2):
        height = 0
        for col, (title, fields) in enumerate(PROJECTS[i:i + 2]):
            block = [section(title, COL_W)] + [kv_line(k, v, COL_W) for k, v in fields]
            lines += [(xs[col], row + j, l) for j, l in enumerate(block)]
            height = max(height, len(block))
        row += height + 1
    lines.append((xs[0], row, kv_line("More", MORE, (xs[1] - xs[0]) * 10 // 96 + COL_W)))  # spans both columns
    height = top + row * lh + 22
    body = "\n".join(f'<tspan x="{x}" y="{top + r * lh}">{l}</tspan>' for x, r, l in lines)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,'JetBrains Mono','DejaVu Sans Mono',monospace" width="985px" height="{height}px" font-size="16px">
<style>
.k {{fill: {c["key"]};}}
.v {{fill: {c["value"]};}}
.m {{fill: {c["muted"]};}}
text, tspan {{white-space: pre; font-variant-ligatures: none;}}
</style>
<rect width="985px" height="{height}px" fill="{c["bg"]}" rx="15"/>
<text x="20" y="30" fill="{c["text"]}" xml:space="preserve">
{body}
</text>
</svg>
'''


def main():
    token = os.environ.get("GH_TOKEN", "").strip()
    today = dt.date.today()
    cache = ROOT / "scripts" / "stats.json"
    if "--offline" in sys.argv and cache.exists():   # re-render without hitting the API
        stats = json.loads(cache.read_text())
    else:
        stats = collect(token)
        cache.write_text(json.dumps(stats, indent=2) + "\n")
    print(json.dumps(stats))
    for theme in THEMES:
        (ROOT / f"{theme}_mode.svg").write_text(render(theme, stats, today))
        (ROOT / f"projects_{theme}.svg").write_text(render_projects(theme))


if __name__ == "__main__":
    main()
