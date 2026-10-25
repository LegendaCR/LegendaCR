<!-- GitHub Profile README · LegendaCR · Ilya Matveevsky · EN -->

<p align="right">
  <a href="https://github.com/LegendaCR/LegendaCR/blob/main/README.ru.md"><img src="./assets/lang-en.svg" height="30" alt="Переключить на русский" title="Читать на русском" /></a>
</p>

<a href="https://legenda-store.ru">
  <img src="./assets/hero-en.svg" width="100%" alt="Ilya Matveevsky — Fullstack Developer. Telegram products and web systems for business" />
</a>

<p align="center">
  <a href="https://legenda-store.ru"><img src="https://img.shields.io/badge/legenda--store.ru-0b0d12?style=for-the-badge&logo=googlechrome&logoColor=93c5fd" alt="Website" /></a>
  <a href="https://t.me/Legenda_CR"><img src="https://img.shields.io/badge/Telegram-0b0d12?style=for-the-badge&logo=telegram&logoColor=93c5fd" alt="Telegram" /></a>
  <a href="https://t.me/legasu"><img src="https://img.shields.io/badge/Channel_@legasu-0b0d12?style=for-the-badge&logo=telegram&logoColor=93c5fd" alt="Telegram channel" /></a>
  <a href="https://gitverse.ru/LegendaCR"><img src="https://img.shields.io/badge/GitVerse-0b0d12?style=for-the-badge&logo=git&logoColor=93c5fd" alt="GitVerse" /></a>
</p>

<img src="./assets/stats-en.svg" width="100%" alt="07 production projects · ~2.5 years of commercial development · Full-cycle · SPbPU" />

<br />

## ◆ About

Fullstack developer based in Saint Petersburg, studying **Software Engineering at Peter the Great St. Petersburg Polytechnic University (SPbPU)**. For the last ~2.5 years I've been building commercial products end to end: I take a business goal, design the architecture, write the frontend and backend, wire up payments, deploy to my own servers and keep things running after launch.

My focus is the **Telegram ecosystem** — bots, Mini Apps and SaaS platforms with built-in monetization — plus web systems (CRM / CMS / client dashboards) and websites.

<table>
  <tr>
    <td width="33%" valign="top">
      <img src="./assets/icons/bot.svg" width="40" alt="" /><br />
      <b>Telegram Bots</b><br />
      <sub>Payments &amp; Telegram Stars, FSM flows, in-bot admin panels, channel access control, anti-spam</sub>
    </td>
    <td width="33%" valign="top">
      <img src="./assets/icons/miniapp.svg" width="40" alt="" /><br />
      <b>Mini Apps</b><br />
      <sub>React clients inside Telegram, server-side <code>initData</code> verification, JWT, leaderboards, seasons, monetization</sub>
    </td>
    <td width="33%" valign="top">
      <img src="./assets/icons/saas.svg" width="40" alt="" /><br />
      <b>SaaS Platforms</b><br />
      <sub>Subscriptions, pricing plans, billing, payment provider webhooks, multi-bot architecture</sub>
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <img src="./assets/icons/web.svg" width="40" alt="" /><br />
      <b>Web Systems</b><br />
      <sub>CRM / CMS, roles &amp; permissions, client dashboards, documents &amp; file storage, analytics</sub>
    </td>
    <td width="33%" valign="top">
      <img src="./assets/icons/site.svg" width="40" alt="" /><br />
      <b>Websites</b><br />
      <sub>Landing pages, corporate and multi-page sites — responsive and polished down to the details</sub>
    </td>
    <td width="33%" valign="top">
      <img src="./assets/icons/infra.svg" width="40" alt="" /><br />
      <b>Infrastructure</b><br />
      <sub>Linux, Docker, nginx, PM2, Cloudflare Tunnel, SSL, backups, health checks, deploy scripts</sub>
    </td>
  </tr>
</table>

<br />

## ◆ Stack

<p>
  <img src="https://skillicons.dev/icons?i=ts,js,react,vite,html,css,tailwind&theme=dark" alt="Frontend" />
  <br />
  <img src="https://skillicons.dev/icons?i=nodejs,express,postgres,docker,nginx,cloudflare,linux,arch,ubuntu&theme=dark" alt="Backend & Infra" />
  <br />
  <img src="https://skillicons.dev/icons?i=git,github,gitlab,vscode,vim&theme=dark" alt="Tools" />
</p>

| Layer | Technologies |
| :-- | :-- |
| **Frontend** | TypeScript, React, Vite, React Router, HTML / CSS |
| **Backend** | Node.js, Express, REST APIs, JWT, Zod, FSM-based flows |
| **Telegram** | Bot API, Telegraf, Mini Apps, Telegram Stars, webhooks |
| **Data** | PostgreSQL, migrations, backups, XLSX import, fuzzy search (Fuse.js) |
| **DevOps** | Docker, nginx, PM2, Cloudflare Tunnel, Linux (Arch / Ubuntu) |

<br />

## ◆ Featured Projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Verdikt Base</h3>
      <sub><b>Telegram Mini App · private community</b></sub>
      <p>A navigation app for members of Maxim Verdikt's community: one entry point to breakdowns, podcasts, streams and chats instead of pinned posts and manual channel searching.</p>
      <p>
        ▸ Bento-style home, content search, Chats / Profile tabs<br />
        ▸ Access gated by channel subscription: <code>initData</code> → JWT<br />
        ▸ Embedded and standalone admin panel, content CRUD, media uploads<br />
        ▸ Bot with a Web App button, webhooks, health checks, DB backups
      </p>
      <p><code>TypeScript</code> <code>React</code> <code>Express</code> <code>PostgreSQL</code> <code>Zod</code> <code>Telegraf</code></p>
      <a href="https://t.me/verdikt_menu_bot">→ @verdikt_menu_bot</a>
    </td>
    <td width="50%" valign="top">
      <h3>Attract Platform</h3>
      <sub><b>Telegram SaaS · channel monetization</b></sub>
      <p>A commercial platform for paid subscriptions to Telegram channels. I owned the architecture, backend, bots and launch infrastructure.</p>
      <p>
        ▸ SaaS bot for channel owners + Gatekeeper bots for subscribers<br />
        ▸ Pricing plans, billing, multiple payment flows<br />
        ▸ Automatic access provisioning, auto-kick, notifications<br />
        ▸ Docker + nginx + Cloudflare Tunnel
      </p>
      <p><code>Node.js</code> <code>Express</code> <code>PostgreSQL</code> <code>Bot API</code> <code>Docker</code></p>
      <a href="https://t.me/attractsub_bot">→ @attractsub_bot</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Brain Train</h3>
      <sub><b>Telegram Mini App · brain training games</b></sub>
      <p>Daily workouts for memory, attention and logic: timed quizzes, arcade mini-games, leaderboards and seasons.</p>
      <p>
        ▸ Server-side score validation — a leaderboard you can't cheat<br />
        ▸ Monetization: Telegram Stars + a payment provider<br />
        ▸ Monorepo: Mini App, API, bot, landing page<br />
        ▸ Migrations, payment webhooks, deploy scripts
      </p>
      <p><code>TypeScript</code> <code>React</code> <code>Vite</code> <code>Express</code> <code>PostgreSQL</code> <code>nginx</code></p>
      <a href="https://t.me/braintrainru_bot">→ @braintrainru_bot</a>
    </td>
    <td width="50%" valign="top">
      <h3>Safronic</h3>
      <sub><b>Business system · furniture assembly</b></sub>
      <p>A website with a client dashboard and two Telegram bots on a shared backend: requests submitted in the bot show up in the dashboard instantly.</p>
      <p>
        ▸ Ordering, assembly, measurement and quote flows, tax ID validation<br />
        ▸ In-bot admin: requests, statuses, replies to clients<br />
        ▸ Quote calculator bot over XLSX price lists with fuzzy search<br />
        ▸ Dashboard with analytics and file storage
      </p>
      <p><code>React</code> <code>Express</code> <code>PostgreSQL</code> <code>Fuse.js</code> <code>xlsx</code> <code>Docker</code></p>
      <a href="https://safronic.ru">→ safronic.ru</a> · <a href="https://t.me/safroninc_bot">@safroninc_bot</a> · <a href="https://t.me/safronic_calc_bot">@safronic_calc_bot</a>
    </td>
  </tr>
</table>

<details>
<summary><b>More projects</b></summary>
<br />

| Project | What it is | Stack |
| :-- | :-- | :-- |
| [**Legend Defense Bot**](https://t.me/Legend_defense_bot) | Anti-spam for groups and channels: filtering, text normalization against bypass tricks, profanity filter | Node.js, Bot API |
| [**@all Bot**](https://t.me/Legend_all_bot) | Mentions every chat member with a single command | Node.js, Bot API |
| **FunPay Automation** | Auto-replies, automatic listing bumps, scheduled chat messages | Node.js |
| **CRM / CMS / websites** | Custom internal management systems and corporate websites | React, Node.js, PostgreSQL |

</details>

<br />

## ◆ How I Work

- **Production-first.** A project is done when it's deployed, monitored and backed up — not when it "works on my machine".
- **Secure by default.** Telegram `initData` signatures are verified on the server, input is validated with schemas (Zod), and anything critical — scores, access, payments — is computed on the backend.
- **Payments without surprises.** Webhooks with signature checks and idempotent processing, clear statuses, admin notifications.
- **I own the full cycle.** Architecture → UI → API → database → server → support. No need to assemble a team for an MVP.

<br />

<p align="center">
  <a href="https://t.me/Legenda_CR"><b>Let's talk about your project →</b></a>
  &nbsp;·&nbsp;
  <a href="https://legenda-store.ru">Portfolio &amp; pricing</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/legasu">Dev channel</a>
</p>

<p align="center">
  <sub><i>Learn, build, automate. Share what I know.</i></sub>
  <br />
  <img src="https://komarev.com/ghpvc/?username=LegendaCR&style=flat-square&color=0b0d12&label=profile+views" alt="Profile views" />
</p>
