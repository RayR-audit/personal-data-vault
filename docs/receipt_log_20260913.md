# 探针收据日志（9/13 首批）

| Date | Channel | Action | Response type | Substance? |
|------|---------|--------|---------------|-----------|
| 2026-09-13 | GitHub x402-foundation/x402 | Issue #3467 (Slack invite request, RayR-audit) | 发布成功，待基金会回复 | — |
| 2026-09-13 | Reddit r/ActivityWatch | 主帖 "Do you actually look back at your ActivityWatch data?" (u/Consistent_Sink2240) | 上线 ✓ https://www.reddit.com/r/ActivityWatch/comments/1wf86wg/ | 待观察 |
| 2026-09-13 | Reddit r/QuantifiedSelf | 评论回复 1vzeeij（数据聚合器帖） | ❌ 未上线（低 karma 静默拒绝，JSON API 确认 0） | — |
| 2026-09-13 | Reddit r/selfhosted | 主帖（本地 SQLite 聚合器） | ❌ 未上线（submit 点击后无跳转无报错，疑似版规门槛静默拦截） | — |

## 结论
- 2/4 发送成功（GitHub issue + r/ActivityWatch 主帖），2/4 被 Reddit 平台静默拦截
- 根因：Consistent_Sink2240 为新号（0 karma），r/QuantifiedSelf 与 r/selfhosted 均有发帖/评论门槛
- 下一步：不重试轰炸；养号 7 天（r/ActivityWatch 内先互动攒 karma）后再攻 r/QuantifiedSelf / r/selfhosted
- 9/16 验收判据回看：r/ActivityWatch 帖实质回复 ≥1 = 过线


## 9/13 晚补发（flair 修复后）
| Date | Channel | Action | Response | Substance? |
|------|---------|--------|----------|-----------|
| 2026-09-13 | Reddit r/selfhosted | 主帖 "Self-hosted attention tracker..." + 必填 flair=Need Help | ⚠️ 一度上线（1wf8z3i），**后被 AutoModerator 删除**：Rule 6 自推项目须发当期 New Project Megathread（old.reddit 回读实锤 22:40） | — |

### 复盘（ Charles 指出 flair 未填 → 根因修正）
- r/selfhosted 主帖首推失败的真实根因 = **必填 flair 未选**（Charles 截图发现），非 karma 门槛
- Reddit 风控静默拒绝的判断部分成立（r/QuantifiedSelf 评论仍未上线），但 selfhosted 是表单校验问题
- 教训：提交前应全扫表单必填项（r-form-validation-message 字段清单），不能只填标题正文
- flair 选择=Need Help（与内容匹配：求反馈）
- **22:40 追加教训**：上线 ≠ 存活。flair 修复后帖子通过表单校验，但随后被版规机器人删除——发布后必须二次回读（含评论区），不能以 submit 跳转成功为终点。版规门槛（Megathread 要求）在发帖前查版规页可预防。

### 当前实况（22:40 裸 CDP 回读 9221 实例）
| 帖 | 状态 | 评论 |
|---|---|---|
| r/ActivityWatch 1wf86wg | ✅ 在线，score 1 | 0 条 |
| r/selfhosted 1wf8z3i | ❌ 被 AutoModerator 删除（Rule 6 → Megathread） | 仅删帖通知 |
| GitHub issue #3467 | ✅ Open，无基金会回复（22:35 web_extract） | 0 |

### 待拍板：r/selfhosted 重发路径 → ✅ 已拍板（09-13 晚，Charles：B）
- **拍板 B**：放弃 r/selfhosted 重发（不进 Megathread），专注养号 + 观察 r/ActivityWatch 帖
- r/selfhosted 线关闭；ActivityWatch 帖为核心探针，24h 无实质回复再议
- 养号窗口：r/ActivityWatch 内互动攒 karma，7 天后（≈9/20）再攻 r/QuantifiedSelf
