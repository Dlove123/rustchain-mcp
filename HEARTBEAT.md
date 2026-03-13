# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

---

## 🚨 每次心跳必读

**每次心跳检查时，必须先读取**：

1. `MEMORY.md` — 核心信息（官方注入）
2. `bounty-hunter/DAILY-LOG-YYYYMMDD.md` — 今日任务进展（关键！）

**如果刚醒来/新会话**：
- 立即读取 MEMORY.md + DAILY-LOG-今天日期.md
- 回答主人验证问题
- 汇报当前状态（证明没失忆）

---

## 📋 心跳检查清单

- [ ] 读取 MEMORY.md
- [ ] 读取 DAILY-LOG-今天日期.md
- [ ] 检查任务进展
- [ ] 检查 GitHub 回复
- [ ] 检查收款状态
- [ ] 整点时汇报
- [ ] **检查整点汇报待发送标记**（.hourly-report-pending.md）
  - 如果存在 → 通过 message 工具发送钉钉消息
  - 发送后 → 标记为已发送（重命名为 .sent.*）

---

*MEMORY.md + DAILY-LOG = 永不失忆！*
