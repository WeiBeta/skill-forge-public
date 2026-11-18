# Quickstart / 快速开始

1. Read the [project charter template](../templates/project/AGENTS.md). In your own project, name the goal, controller, domain authority and existing rules. Use the templates you need; keep existing governance and records intact.
2. Choose the `forge-*` skills you need and confirm your harness can discover them. For a PM, use [PM management](../skills/forge-pm-management/SKILL.md) to bind the actual execution, receiving and notification tools; then use [work dispatch](../skills/forge-work-dispatch/SKILL.md) against that contract. Keep both skill directories and their references together.
3. Try [a small, reversible task](../examples/task.md) with explicit inputs, write scope, verification and handoff. Name an independent reviewer only when the risk or project contract calls for one.
4. Choose [native Codex](../adapters/codex-native/README.md) or the [optional OpenCodex route](../adapters/opencodex/README.md) according to actual capabilities. Keep example settings as references until the target host and authority have been checked.
5. Verify the shipped files with the [public source tool](PACKAGES.md). Record separately the runtime checks you ran in your own environment.

先用一个小任务跑完整流程，再增加并发。对安装、发现、加载、使用和效果分别核实；公开包是工程范本及技能，未运行目标环境。
