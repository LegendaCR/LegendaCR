<!-- GitHub Profile README · LegendaCR · Ilya Matveevsky -->

<a href="https://legenda-store.ru">
  <img src="./assets/hero.svg" width="100%" alt="Илья Матвеевский — Fullstack Developer. Telegram-продукты и web-системы для бизнеса" />
</a>

<p align="center">
  <a href="https://legenda-store.ru"><img src="https://img.shields.io/badge/legenda--store.ru-0b0d12?style=for-the-badge&logo=googlechrome&logoColor=93c5fd" alt="Website" /></a>
  <a href="https://t.me/Legenda_CR"><img src="https://img.shields.io/badge/Telegram-0b0d12?style=for-the-badge&logo=telegram&logoColor=93c5fd" alt="Telegram" /></a>
  <a href="https://t.me/legasu"><img src="https://img.shields.io/badge/Канал_@legasu-0b0d12?style=for-the-badge&logo=telegram&logoColor=93c5fd" alt="Telegram channel" /></a>
  <a href="https://gitverse.ru/LegendaCR"><img src="https://img.shields.io/badge/GitVerse-0b0d12?style=for-the-badge&logo=git&logoColor=93c5fd" alt="GitVerse" /></a>
</p>

<img src="./assets/stats.svg" width="100%" alt="07 production-проектов · ~2.5 года коммерческой разработки · Full-cycle · СПбПУ" />

<br />

## ◆ Обо мне

Fullstack-разработчик из Санкт-Петербурга (**СПбПУ, программная инженерия**). Последние ~2.5 года делаю коммерческие продукты под ключ: беру задачу на уровне бизнес-цели, проектирую архитектуру, пишу фронт и бэк, подключаю платежи, разворачиваю на своём сервере и поддерживаю после запуска.

Специализация — **экосистема Telegram**: боты, Mini Apps и SaaS-платформы с монетизацией. Плюс web-системы (CRM / CMS / личные кабинеты) и сайты.

<table>
  <tr>
    <td width="33%" valign="top">
      <b>🤖 Telegram-боты</b><br />
      <sub>Платежи и Telegram Stars, FSM-сценарии, админки внутри бота, выдача доступа в каналы, антиспам</sub>
    </td>
    <td width="33%" valign="top">
      <b>📱 Mini Apps</b><br />
      <sub>React-клиенты внутри Telegram, проверка <code>initData</code>, JWT, рейтинги, сезоны, монетизация</sub>
    </td>
    <td width="33%" valign="top">
      <b>💳 SaaS-платформы</b><br />
      <sub>Подписки, тарифы, биллинг, вебхуки платёжных провайдеров, мультибот-архитектура</sub>
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <b>🗂 Web-системы</b><br />
      <sub>CRM / CMS, роли и права, личные кабинеты, документы и файлы, статистика</sub>
    </td>
    <td width="33%" valign="top">
      <b>🌐 Сайты</b><br />
      <sub>Лендинги, корпоративные и многостраничные проекты с адаптивом и вниманием к деталям</sub>
    </td>
    <td width="33%" valign="top">
      <b>⚙️ Инфраструктура</b><br />
      <sub>Linux, Docker, nginx, PM2, Cloudflare Tunnel, SSL, бэкапы, health-check, CI-скрипты деплоя</sub>
    </td>
  </tr>
</table>

<br />

## ◆ Стек

<p>
  <img src="https://skillicons.dev/icons?i=ts,js,react,vite,html,css,tailwind&theme=dark" alt="Frontend" />
  <br />
  <img src="https://skillicons.dev/icons?i=nodejs,express,postgres,docker,nginx,cloudflare,linux,arch,ubuntu&theme=dark" alt="Backend & Infra" />
  <br />
  <img src="https://skillicons.dev/icons?i=git,github,gitlab,vscode,vim&theme=dark" alt="Tools" />
</p>

| Слой | Технологии |
| :-- | :-- |
| **Frontend** | TypeScript, React, Vite, React Router, HTML / CSS |
| **Backend** | Node.js, Express, REST API, JWT, Zod, FSM-сценарии |
| **Telegram** | Bot API, Telegraf, Mini Apps, Telegram Stars, webhooks |
| **Data** | PostgreSQL, миграции, бэкапы, XLSX-импорт, fuzzy-поиск (Fuse.js) |
| **DevOps** | Docker, nginx, PM2, Cloudflare Tunnel, Linux (Arch / Ubuntu) |

<br />

## ◆ Избранные проекты

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>База Вердикта</h3>
      <sub><b>Telegram Mini App · закрытое сообщество</b></sub>
      <p>Навигационное приложение для участников сообщества Максима Вердикта: единая точка входа к разборам, подкастам, стримам и чатам вместо закрепов и ручного поиска.</p>
      <p>
        ▸ Bento-главная, поиск по материалам, вкладки «Чаты» / «Профиль»<br />
        ▸ Доступ по подписке на канал: <code>initData</code> → JWT<br />
        ▸ Встроенная и отдельная админ-панель, CRUD контента, медиа<br />
        ▸ Бот с Web App-кнопкой, webhook, health-check, бэкапы БД
      </p>
      <p><code>TypeScript</code> <code>React</code> <code>Express</code> <code>PostgreSQL</code> <code>Zod</code> <code>Telegraf</code></p>
      <a href="https://t.me/verdikt_menu_bot">→ @verdikt_menu_bot</a>
    </td>
    <td width="50%" valign="top">
      <h3>Attract Platform</h3>
      <sub><b>Telegram SaaS · монетизация каналов</b></sub>
      <p>Коммерческая платформа платных подписок на Telegram-каналы. Отвечал за архитектуру, backend, ботов и инфраструктуру запуска.</p>
      <p>
        ▸ SaaS-бот для владельцев каналов + Gatekeeper-боты для подписчиков<br />
        ▸ Тарифы, биллинг, несколько сценариев оплаты<br />
        ▸ Автоматическая выдача доступа, автокик, уведомления<br />
        ▸ Docker + nginx + Cloudflare Tunnel
      </p>
      <p><code>Node.js</code> <code>Express</code> <code>PostgreSQL</code> <code>Bot API</code> <code>Docker</code></p>
      <a href="https://t.me/attractsub_bot">→ @attractsub_bot</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Brain Train</h3>
      <sub><b>Telegram Mini App · игры для мозга</b></sub>
      <p>Тренировки памяти, внимания и логики: таймерные викторины, аркадные мини-игры, рейтинги и сезоны.</p>
      <p>
        ▸ Серверная валидация очков — защита рейтинга от накрутки<br />
        ▸ Монетизация: Telegram Stars + платёжный провайдер<br />
        ▸ Monorepo: Mini App, API, бот, лендинг<br />
        ▸ Миграции, платёжные вебхуки, скрипты выкладки
      </p>
      <p><code>TypeScript</code> <code>React</code> <code>Vite</code> <code>Express</code> <code>PostgreSQL</code> <code>nginx</code></p>
      <a href="https://t.me/braintrainru_bot">→ @braintrainru_bot</a>
    </td>
    <td width="50%" valign="top">
      <h3>Safronic</h3>
      <sub><b>Бизнес-система · сборка мебели</b></sub>
      <p>Сайт с личным кабинетом и два Telegram-бота, связанные общим backend: заявки из бота сразу появляются в ЛК.</p>
      <p>
        ▸ Сценарии заказа, сборки, замера и просчёта, проверка ИНН<br />
        ▸ Админка в боте: заявки, статусы, ответ клиенту<br />
        ▸ Бот-калькулятор по XLSX-прайсам с fuzzy-поиском<br />
        ▸ ЛК со статистикой и файлами
      </p>
      <p><code>React</code> <code>Express</code> <code>PostgreSQL</code> <code>Fuse.js</code> <code>xlsx</code> <code>Docker</code></p>
      <a href="https://safronic.ru">→ safronic.ru</a> · <a href="https://t.me/safroninc_bot">@safroninc_bot</a> · <a href="https://t.me/safronic_calc_bot">@safronic_calc_bot</a>
    </td>
  </tr>
</table>

<details>
<summary><b>Ещё проекты</b></summary>
<br />

| Проект | Что это | Стек |
| :-- | :-- | :-- |
| [**Legend Defense Bot**](https://t.me/Legend_defense_bot) | Антиспам для групп и каналов: фильтрация, нормализация текста против обходов, анти-мат | Node.js, Bot API |
| [**@all Bot**](https://t.me/Legend_all_bot) | Массовое упоминание участников чата по команде | Node.js, Bot API |
| **FunPay Automation** | Автоответы, автоподнятие лотов, периодические сообщения в чаты | Node.js |
| **CRM / CMS / сайты** | Внутренние системы управления и корпоративные сайты под заказ | React, Node.js, PostgreSQL |

</details>

<br />

## ◆ Как я работаю

- **Production-first.** Проект считается готовым, когда он задеплоен, мониторится и бэкапится, а не когда «работает у меня».
- **Безопасность по умолчанию.** Подпись Telegram `initData` проверяется на сервере, входные данные валидируются схемами (Zod), всё критичное (очки, доступы, платежи) считается на backend.
- **Платежи без сюрпризов.** Вебхуки с проверкой подписи и идемпотентной обработкой, понятные статусы, уведомления админам.
- **Владею всем циклом.** Архитектура → UI → API → БД → сервер → поддержка. Заказчику не нужно собирать команду под MVP.

<br />

## ◆ Активность

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=LegendaCR&bg_color=05060a&color=c9d3ea&line=93c5fd&point=a5b4fc&area=true&area_color=3b5bdb&hide_border=true&radius=16" width="100%" alt="GitHub activity graph" />
</p>

<br />

<p align="center">
  <a href="https://t.me/Legenda_CR"><b>Обсудить задачу →</b></a>
  &nbsp;·&nbsp;
  <a href="https://legenda-store.ru">Портфолио и цены</a>
  &nbsp;·&nbsp;
  <a href="https://t.me/legasu">Канал с разборами</a>
</p>

<p align="center">
  <sub><i>Изучаю, создаю, автоматизирую. Делюсь опытом.</i></sub>
  <br />
  <img src="https://komarev.com/ghpvc/?username=LegendaCR&style=flat-square&color=0b0d12&label=profile+views" alt="Profile views" />
</p>
