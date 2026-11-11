# Engineering structure / 工程结构

Use three layers: a short project charter, role-specific guidance, and records tied to the work. Start with [one bounded task](../examples/task.md); add roles and coordination only when work can be isolated.

| Layer | Responsibility | Entry |
| --- | --- | --- |
| Governance | Project scope, authority, roles and one integration owner | [Project charter](../templates/project/AGENTS.md) |
| Skills | Reusable procedures for instructions, review, diagnosis, modeling, dispatch, agent recovery and ledger reconciliation | [Work dispatch](../skills/forge-work-dispatch/SKILL.md) |
| Adapters | Version-sensitive host capabilities and example configuration | [Native Codex](../adapters/codex-native/README.md), [optional OpenCodex](../adapters/opencodex/README.md) |
| Evidence | Fixed inputs, candidate identity, results, handoff and recovery | [Management protocol](../templates/project/docs/MANAGEMENT.md), [recovery](DEPLOYMENT-RECOVERY.md) |

The controller owns scope, integration and acceptance. A PM can coordinate independent work and return substantive results. Give the executor a whole work package: implementation, focused checks, and evidence. Split it only for a real conflict, permission boundary, or need for independently useful work or review. Formal independent review comes from someone who did not implement the candidate. Check the task instance, worktree and shared resources separately.

先读[快速开始](QUICKSTART.md)，按项目规模裁剪职责。能力合同和[权限说明](PERMISSIONS.md)约束配置示例的使用范围；[验收指南](VALIDATION.md)说明静态与实测的区别。
