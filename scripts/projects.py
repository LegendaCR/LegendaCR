"""Project cards for the profile README: one full-width card per project.

Order, texts, stacks, links and logos mirror the portfolio site (legenda-store.ru/projects).
Each card is its own SVG so the README can wrap it in a link to that project.
"""
import base64
import html
import textwrap

PROJECTS = [
    {
        "slug": "crm", "logo": "crm.png",
        "title": "CRM / CMS / CIS systems", "kind": "Internal web systems",
        "about": "Internal products for roles, documents, statuses and business workflows.",
        "task": "Replace fragmented manual operations with one system and explicit permissions and states.",
        "solution": "React workspaces, Node.js APIs, PostgreSQL, role-based access, documents, directories, filters and integrations.",
        "result": "An extensible production architecture for daily operational work.",
        "stack": ["React", "Node.js", "PostgreSQL", "REST API", "RBAC", "CMS", "CRM"],
        "link": "https://safronic.ru",
    },
    {
        "slug": "size-of-space", "logo": "size-of-space.png",
        "title": "Size of Space", "kind": "Interactive WebGL site",
        "about": "A journey through the scale of the universe: 79 objects from asteroid Bennu to the whole observable universe.",
        "task": "Show the size of cosmic objects across 24 orders of magnitude, so each object is always seen against the one before it.",
        "solution": "A Three.js 3D scene with real NASA and USGS maps, ray-traced Saturn rings and procedural GLSL shaders for stars, black holes and galaxies. Compare mode for any two objects and generative music on the Web Audio API.",
        "result": "A light static site with one runtime dependency, rendering in real time. RU/EN, a shareable link for every object, trackpad, keyboard and swipe navigation. Open source.",
        "stack": ["TypeScript", "Three.js", "WebGL", "GLSL shaders", "Web Audio API", "Vite", "i18n"],
        "link": "https://legendacr.github.io/size-of-space/",
    },
    {
        "slug": "attract", "logo": "attract.png",
        "title": "Attract Platform", "kind": "Telegram SaaS",
        "about": "A commercial platform for monetising channels through paid subscriptions.",
        "task": "Bring plan management, payments and subscriber access into one product for channel administrators.",
        "solution": "An admin SaaS bot, dedicated gatekeeper bots, billing, access provisioning, automatic removal and service notifications.",
        "result": "A production stack backed by PostgreSQL, Docker, nginx and Cloudflare Tunnel.",
        "stack": ["Node.js", "Express", "PostgreSQL", "Telegram Bot API", "Docker", "nginx", "Cloudflare Tunnel"],
        "link": "https://t.me/attractsub_bot",
    },
    {
        "slug": "brain-train", "logo": "brain-train.png",
        "title": "Brain Train", "kind": "Telegram Mini App",
        "about": "A game platform for memory, attention and logic training.",
        "task": "Build a Mini App with multiple game modes, ratings, seasons and monetisation.",
        "solution": "A TypeScript/React client, REST API with server-side score validation, Telegram bot, JWT, migrations, Stars and payment webhooks.",
        "result": "A complete production stack using PostgreSQL, nginx, PM2 and a dedicated deployment workflow.",
        "stack": ["TypeScript", "React", "Vite", "Node.js", "Express", "PostgreSQL", "Telegram Stars", "JWT", "nginx"],
        "link": "https://t.me/braintrainru_bot",
    },
    {
        "slug": "verdikt", "logo": "verdikt.png",
        "title": "Verdikt Base", "kind": "Telegram Mini App",
        "about": "A private navigation app for Maks Verdikt's community: all content and chats in one place.",
        "task": "Replace long pinned posts and manual channel searches with a single entry point available only to subscribers.",
        "solution": "A monorepo with a TypeScript React/Vite client (bento home, chats, profile, search), an Express API with initData validation, JWT and subscription-gated access, a bot with a Web App button and an admin panel for sections, chats, banners and media.",
        "result": "A production app with gated access, manageable content and a moderator admin panel on PostgreSQL, nginx and PM2, with health checks and database backups.",
        "stack": ["TypeScript", "React", "Vite", "Node.js", "Express", "PostgreSQL", "JWT", "Zod", "Telegraf", "nginx", "PM2"],
        "link": "https://t.me/verdikt_menu_bot",
    },
    {
        "slug": "ai-news", "logo": "ai-news.png",
        "title": "AI News", "kind": "AI automation",
        "about": "A self-running Telegram channel about AI news, with an AI model finding, verifying and writing every post.",
        "task": "Run a news channel with no human editor: find fresh stories, check them against the primary source, avoid repeats and publish on schedule.",
        "solution": "An AI model acts as the editor: web search, article reading, X and Threads posts and strict structured output. The model is swappable (Claude, GPT, Gemini). Several post formats and rubrics, Playwright source screenshots, videos and albums.",
        "result": "8 posts a day with no human involvement. Runs in Docker, with dry-run mode, manual publishing and failure alerts to the admin.",
        "stack": ["Python", "LLM API", "Claude / GPT / Gemini", "Tool use", "Web search", "Playwright", "Telegram Bot API", "Docker"],
        "link": "https://t.me/A1News_world",
    },
    {
        "slug": "safronic", "logo": "safronic.png",
        "title": "Safronic Bot", "kind": "Business bot",
        "about": "A Telegram bot for furniture assembly requests.",
        "task": "Structure requests from different client types and eliminate manual data transfers.",
        "solution": "Branching FSM workflows, tax ID validation, file uploads, thread-specific alerts and follow-up reminders.",
        "result": "One predictable channel for receiving and processing orders.",
        "stack": ["Node.js", "Telegram Bot API", "FSM", "Files", "Notifications"],
        "link": "https://t.me/safroninc_bot",
    },
    {
        "slug": "legend-defense", "logo": "legend-bots.png",
        "title": "Legend Defense Bot", "kind": "Moderation bot",
        "about": "An anti-spam system for Telegram groups and channels.",
        "task": "Block links, banned terms and obfuscated spelling without constant manual moderation.",
        "solution": "Text normalisation, configurable dictionaries, fuzzy matching and moderator controls inside Telegram.",
        "result": "Automated filtering for complex spam patterns with in-chat administration.",
        "stack": ["Node.js", "Telegram Bot API", "JSON", "Normalization", "Fuzzy matching"],
        "link": "https://t.me/Legend_defense_bot",
    },
    {
        "slug": "all-bot", "logo": "legend-bots.png",
        "title": "@all Bot", "kind": "Utility bot",
        "about": "A focused tool for mentioning group administrators.",
        "task": "Alert the right participants quickly without spam or command abuse.",
        "solution": "Permission checks, filtering users without usernames, anti-flood controls and clear service responses.",
        "result": "A small, dependable utility for operational Telegram groups.",
        "stack": ["Node.js", "Telegram Bot API", "Permissions", "Anti-flood"],
        "link": "https://t.me/Legend_all_bot",
    },
]

WIDTH, LH = 985, 20
TEXT_X, LOGO = 132, 88       # text column start, logo size in px
WRAP = 84                    # characters per line in the text column
PREFIX = 14                  # ". Solution: . " -> values start at this column
FONT = "ConsolasFallback,Consolas,'JetBrains Mono','DejaVu Sans Mono',monospace"


def span(cls, s):
    return f'<tspan class="{cls}">{html.escape(s)}</tspan>'


def field(key, value, cls="v"):
    """'. Key: .... value' with the value wrapped and continuation lines aligned under it."""
    head = f". {key}: "
    dots = "." * max(1, PREFIX - len(head) - 1) + " "
    rows = textwrap.wrap(value, WRAP - PREFIX) or [""]
    first = span("m", ". ") + span("k", key) + ":" + span("m", " " + dots) + span(cls, rows[0])
    return [first] + [" " * PREFIX + span(cls, r) for r in rows[1:]]


def card_lines(i, p):
    title = f"{i:02d}  {p['title']}"
    rule = "—" * (WRAP - len(title) - len(p["kind"]) - 6)
    lines = [span("m", "- ") + span("t", title) + " " + span("m", rule) + " " + span("k", p["kind"])]
    lines += field("About", p["about"], "x")
    lines += field("Task", p["task"])
    lines += field("Solution", p["solution"])
    lines += field("Result", p["result"])
    lines += field("Stack", " · ".join(p["stack"]), "s")
    lines += field("Link", p["link"].removeprefix("https://").rstrip("/"), "l")
    return lines


def render_card(theme, c, i, p, logo_png):
    lines = card_lines(i, p)
    top = 34
    height = max(top + (len(lines) - 1) * LH, 24 + LOGO) + 26
    body = "\n".join(f'<tspan x="{TEXT_X}" y="{top + n * LH}">{l}</tspan>' for n, l in enumerate(lines))
    logo = base64.b64encode(logo_png).decode()
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" font-family="{FONT}" width="{WIDTH}px" height="{height}px" font-size="16px">
<title>{html.escape(p["title"])} — {html.escape(p["kind"])}</title>
<style>
.k {{fill: {c["key"]};}}
.v {{fill: {c["value"]};}}
.m {{fill: {c["muted"]};}}
.t {{fill: {c["text"]}; font-weight: 700;}}
.x {{fill: {c["text"]};}}
.s {{fill: {c["add"]};}}
.l {{fill: {c["value"]}; text-decoration: underline;}}
text, tspan {{white-space: pre; font-variant-ligatures: none;}}
</style>
<defs><clipPath id="lg"><rect x="24" y="24" width="{LOGO}" height="{LOGO}" rx="20"/></clipPath></defs>
<rect width="{WIDTH}px" height="{height}px" fill="{c["bg"]}" rx="15"/>
<image x="24" y="24" width="{LOGO}" height="{LOGO}" clip-path="url(#lg)" href="data:image/png;base64,{logo}" xlink:href="data:image/png;base64,{logo}"/>
<rect x="24.5" y="24.5" width="{LOGO - 1}" height="{LOGO - 1}" rx="19.5" fill="none" stroke="{c["border"]}"/>
<text x="{TEXT_X}" y="{top}" fill="{c["text"]}" xml:space="preserve">
{body}
</text>
</svg>
'''


def render_header(theme, c):
    line = (span("k", "ilya@legenda") + ":" + span("v", "~") + "$ ls ~/projects "
            + span("m", f"# {len(PROJECTS)} production cases · click a card to open it"))
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="{FONT}" width="{WIDTH}px" height="56px" font-size="16px">
<style>
.k {{fill: {c["key"]};}}
.v {{fill: {c["value"]};}}
.m {{fill: {c["muted"]};}}
text, tspan {{white-space: pre; font-variant-ligatures: none;}}
</style>
<rect width="{WIDTH}px" height="56px" fill="{c["bg"]}" rx="15"/>
<text x="24" y="34" fill="{c["text"]}" xml:space="preserve">{line}</text>
</svg>
'''


def write_all(root, themes):
    out = root / "projects"
    out.mkdir(exist_ok=True)
    for theme, c in themes.items():
        (out / f"00-header-{theme}.svg").write_text(render_header(theme, c))
        for i, p in enumerate(PROJECTS, 1):
            png = (root / "assets" / "logos" / p["logo"]).read_bytes()
            (out / f"{i:02d}-{p['slug']}-{theme}.svg").write_text(render_card(theme, c, i, p, png))


def readme_block():
    """Markdown for the README: header + one clickable card per project."""
    def pic(name, alt, link=None):
        tag = (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="./projects/{name}-dark.svg">\n'
               f'  <img alt="{html.escape(alt)}" src="./projects/{name}-light.svg">\n</picture>')
        return f'<a href="{link}">\n{tag}\n</a>' if link else tag
    parts = [pic("00-header", "Projects")]
    for i, p in enumerate(PROJECTS, 1):
        parts.append(pic(f"{i:02d}-{p['slug']}", f"{p['title']} — {p['kind']}: {p['about']}", p["link"]))
    return "\n\n".join(parts)
