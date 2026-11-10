# Buyer/User Probe List (D6-7 · highest-weight action)

> Goal: validate the ONLY unverified assumption — someone else wants this.
> Judging criteria per 7-day acceptance: >=1 SUBSTANTIVE reply (question back, feature ask, or willingness to pay/test),
> NOT just likes/ups. No substantive reply by 09-16 => stop line.

## Target pool (10)

| # | Channel/Target | Why | Status |
|---|----------------|-----|--------|
| 1 | r/ActivityWatch (reddit) | AW users already want aggregation+insight beyond AW | pending |
| 2 | r/degoogle thread "local alternative to cloud time tracking" | exact ICP: local-first time tracking | pending |
| 3 | r/DopamineDetoxing "Alternatives to RescueTime" | RescueTime refugees | pending |
| 4 | forum.quantifiedself.com "Why do self-trackers build their own aggregators" | 2020 thread, still-active community, proven pain | pending |
| 5 | r/selfhosted | self-host audience, tool discoverers | pending |
| 6 | TickTick backup tool users (ticktick-backup github issues) | people who care about owning TickTick data | pending |
| 7 | ActivityWatch forum "How AW could be better" thread | feature-gap demand signal | pending |
| 8 | ingest.sh users (libhunt reviews page) | paying-adjacent SaaS users | pending |
| 9 | Vana community (r/VanaSpotifyProject type) | data-ownership believers | pending |
| 10 | r/productivity RescueTime-alternative threads | broad ICP | pending |

## Send plan: pick 2-3 highest-signal (#1, #4, #7 first), send, log receipt here.

## Probe message (EN, for reddit/forum replies & posts)

> I've been building a small open-source tool (Personal Data Vault) that sits on top of
> ActivityWatch + task apps like TickTick: it aggregates everything into one local SQLite
> file and generates a daily AI insight report — fully local, no cloud, no account.
> Question for this community: is a daily "where did my attention actually go" report +
> one-command full data export something you'd want as a standalone tool, or does your
> current setup (AW alone / RescueTime / spreadsheets) already cover it? Would you pay for
> the AI-insight layer, or is local aggregation only useful if free?
> Repo: https://github.com/RayR-audit/personal-data-vault

## Receipt log

| Date | Channel | Action | Response type | Substance? |
|------|---------|--------|---------------|-----------|
| 2026-10-12 21:2x | GitHub · ActivityWatch Discussions → **Show and tell**（本条替代原 #7 AW 论坛，同一人群、零新增登录） | 发帖 [Discussion #1522](https://github.com/orgs/ActivityWatch/discussions/1522)，身份 RayR-audit；标题 *Personal Data Vault — aggregating ActivityWatch + task data into one local SQLite vault (feedback welcome)*；正文= `docs/probe_message_20261012.md` §一（**问题驱动**：3 个问题，含「你现有方案是否已覆盖」与「免费才用 vs 愿付费」） | 待回读（首发） | ⏳ 待判 |

**读回计划**：48h 内（2026-10-14 前）回读一次评论数/内容；**7 天窗口终点 = 2026-10-19**。
**判据（沿用 9-08 拍板）**：≥1 条**实质性**回复（回问 / 提需求 / 愿测愿付）→ 验收成立；7 天全空 → 按「全空则停」处置。**⚠️ 沉默 ≠ 需求不成立**（公开帖可能只是没被看到），若判停须写清「是沉默而非否定」，并把它与「已证伪」区分开。
**事实核验**：发帖成功且已用**匿名通道**复读确认公开可见（无 cookie GET 返回 200，含 'Show and tell' / 'RayR-audit' / 正文特征串）。

> 口径更正（2026-10-12）：上游曾判「GitHub 通道受**账号或仓库层限制**、三次失败」——**该诊断错误**。本次同账号实发成功；真实障碍是**表单必填项「I have done a search for similar discussions」未勾选**（未勾选时提交只回一句通用错误 `There was an error creating your Discussion`，页面内所有 `flash-error` 均为隐藏模板 → 看不出是必填项问题）。另：fine-grained token 仅授 Discussions **读**权限，GraphQL `createDiscussion` 返回 `FORBIDDEN: Resource not accessible by personal access token`（同一句会被误读成 token 失效）。

---

## 探针终判（2026-11-10 · 窗口过期 22 天后补读）

> 触发：7 天验收窗口终点为 **2026-10-19**，实际回读日 **2026-11-10**（逾期 22 天）。此条为**补做判定**，非新动作。

### 读数（两路交叉，均为今日现读）

| 通道 | 读数 | 证据 |
|---|---|---|
| GitHub Discussions **#1522** | **0 评论**；Upvote **2** | ①HTML 直取：`Replies: 0 comments`（两处一致）②`web_extract` 独立通道：`## Replies: 0 comments`；发布 `2026-10-12T13:14:58Z`；未锁定、公开可见、正文完整 |
| Reddit r/ActivityWatch `1wf86wg`（9-13 副探针） | **未复证** | 今日 403（`www.reddit.com/.json`）、429（`.rss`）、old.reddit 返回空壳页 ⇒ 反爬墙。**不并入结论**；9-13 当时读数为 0 评论 / score 1 |

### 判定

**判据（预注册，2026-10-12 写定）**：≥1 条**实质性**回复（回问 / 提需求 / 愿测愿付）→ 验收成立；7 天全空 → 按「全空则停」处置。

**结论：判据不成立 → 需求端探针线停（不再投递新渠道）。**

**定性（必须与「已证伪」区分）**：
- 这是 **沉默**，不是**否定**。29 天内 2 个 upvote 说明帖子被看过、内容未被反驳；没有任何人写出「我已用 X 覆盖」或「这没用」。
- 沉默的三种可能未被区分：① 该人群不在 GitHub Discussions ② 需求真实但优先级低到不愿打字 ③ 需求不存在。**现有证据无法在三者间裁决**。
- 因此：**不得**把本结论写成「PDV 无市场需求」；正确表述是「**该渠道 × 该问法**在 29 天内未取得任何口头信号」。

### 处置

1. **停投递**：不再为 PDV 开新渠道做需求探针（连续 3 个渠道 × 45 天零实质回应：x402 #3467、AW #1522、Reddit 系）。
2. **不关项目**：repo、dogfood、local-first 定位原样保留；项目降为**自用工具**态，不再以「验证需求」为目标耗工时。
3. **重开条件（预注册，任一即可）**：① 有外部用户主动提 issue / 引用 ② 出现付费意向的具体对话 ③ 有了可免费搭车的分发位（如随 PPV/同类开源项目一起被提及）。届时按「抓到信号再投入」，不做预防性投入。
4. **成本记账**：本线已投入的最大成本是**渠道试错**（3 渠道 4 次被平台静默拦截/删除），不是代码。

### 教训（回填）

- **判据到期没人读 = 判据不存在**：7 天窗口 10-19 到期，直到 11-10 盘点才补读，中间 22 天无人触发。同类形态（产物有、判据有、回读缺）应挂到每日锚闸或卡点哨，不能只写在文档里。
- **「0 评论」与「被删除」必须分开读**：Reddit 那次是平台删帖（假信号），这次是真实 0 回复（真沉默）。两者在台账里不能合并成「Reddit 无效」。
