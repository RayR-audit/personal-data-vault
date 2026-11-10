# Personal Data Vault · 买方探针文案（待 Charles 过目后发）

**投递位置**：ActivityWatch 主仓 Discussions → **Show and tell**（"Show off something you've made"）
**网址**：https://github.com/ActivityWatch/activitywatch/discussions
**身份**：RayR-audit（与 repo `RayR-audit/personal-data-vault` **同线**，不涉及跨线信用借用）
**为何选这里**：AW 主仓 ★19.2k、v0.14.1 刚更新（2026-10-10）、有专门的 Show and tell 类别；AW 用户正是「已经在意本地数据主权」的人群 = 最可能回答"要不要"的人
**性质**：公开、可回读、不点名、不推销；问的是"你会不会用 / 会不会付费"——测的是**需求端**（40 天来唯一没测过的假设）

---

## 一、英文正文（将原样发布）

**Title:** Personal Data Vault — aggregating ActivityWatch + task data into one local SQLite vault (feedback welcome)

**Body:**

I've been running a small open-source tool on top of ActivityWatch for the last month and would value this community's honest read on whether it's actually useful or just something that's useful *to me*.

**What it does**
- Pulls ActivityWatch events (window/afk) plus task data (TickTick export) into **one local SQLite file** — no cloud, no account, no telemetry.
- Generates a **daily insight report** locally from that data ("where did my attention actually go").
- One-command export to JSON/CSV, so nothing is locked in.

**What it deliberately does not do:** no account system, no sync service, no data marketplace, no protocol/on-chain layer. Local-first only.

Repo: https://github.com/RayR-audit/personal-data-vault

**Three questions I'd genuinely like answered**

1. If you already run ActivityWatch, is *local aggregation across multiple sources + a daily digest* something you'd want as a standalone tool — or does your current setup (AW alone, custom scripts, Grafana, spreadsheets) already cover it?
2. Which part is actually missing for you — the aggregation, the digest, or the clean export/ownership angle?
3. If there were a paid layer (e.g. richer local analysis / report templates), would you consider it — or is "local data tooling" something you'd only ever use if it's free?

No pitch here — I'm trying to find out whether the need is real outside my own setup. Blunt answers welcome, including "my existing setup is fine."

---

## 二、中文逐条对照（内部审核用，不外发）

**标题：** Personal Data Vault —— 把 ActivityWatch + 任务数据聚合进一个本地 SQLite 金库（欢迎反馈）

**正文：**

我在 ActivityWatch 之上跑了一个小型开源工具，已经用了一个月。想请这个社区诚实地告诉我：它到底是有用，还是只是"对我自己有用"。

**它做什么**
- 把 ActivityWatch 事件（窗口/AFK）+ 任务数据（TickTick 导出）拉进**一个本地 SQLite 文件**——无云、无账号、无遥测。
- 基于这些数据**在本地**生成每日洞察报告（"我的注意力到底去哪了"）。
- 一条命令导出 JSON/CSV，不锁定。

**它刻意不做的事：** 不做账号体系、不做同步服务、不做数据交易市场、不做协议层/上链层。只做本地优先。

仓库：https://github.com/RayR-audit/personal-data-vault

**我真心想被回答的三个问题**

1. 如果你已经在用 ActivityWatch——「**跨多个源的本地聚合 + 每日摘要**」这件事，你会想要一个独立工具吗？还是你现在的方案（只用 AW、自写脚本、Grafana、表格）已经覆盖了？
2. 对你来说，真正缺的是哪一块——聚合、摘要，还是"干净导出/数据所有权"这个角度？
3. 如果存在付费层（例如更丰富的本地分析 / 报告模板），你会考虑吗？还是"本地数据工具"这种东西你只会在免费时使用？

不是推销——我是在确认这个需求在我自己的环境之外是否真实存在。欢迎直说，包括"我现在的方案挺好"。

---

## 三、发布前机械检查（沿用既有纪律）

- [x] 身份线一致：repo = RayR-audit，发布身份 = RayR-audit（不借 MECIP/@governance_arc）
- [x] 不点名任何主体、不含指控性措辞
- [x] 不含密钥 / 内部路径 / 中文残渣 / 工具归属
- [x] 链接可达性：repo 为公开仓（待发布前未登录 GET 复测一次）
- [x] 中文对照已备（本文件 §二）
- [ ] ⬜ **Charles 过目**（本条即当前状态）

## 四、发送后动作（预案）

1. 回执登记到 `docs/buyer_probes.md` 的 Receipt log（日期/渠道/动作/回应类型/是否实质）
2. 24-48h 内回读一次（未登录 API 抓该 discussion 的评论数）
3. 判据（沿用 9-08 拍板）：**≥1 条实质性回复**（回问 / 提需求 / 愿测愿付）→ 验收成立；否则 7 天窗口结束按「全空则停」处置
4. 同步更新 D17 卡点状态

---
*备选渠道（若这条不合适）：forum.quantifiedself.com「Why do self-trackers build their own aggregators」帖、ActivityWatch 官方论坛「How AW could be better」——两处均需你先登录一次（实测当前浏览器无登录态）。*
