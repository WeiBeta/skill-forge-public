# Task routing and three PM roles / 派工与三类 PM

Choose an executor by the work, then bind the actual model or execution mode available in the project. Keep the route table outside the skills. Trim optional channels at installation and apply route changes to new work or an explicitly resumed order.

按任务选择执行者，在项目内绑定实际可用的模型、模式和参数。路由表独立于技能。初装只启用所需通道，新工单及明确续接采用新路由。

| Work / 工作 | Example route / 选型示例 | Evidence / 核验 |
| --- | --- | --- |
| Repeatable checks / 固定核验 | Script, or Terra 6.1 low / 脚本，必要时用轻量代理 | Fixed input and output / 比对输入与输出 |
| Governance and skill changes / 工程约束与技能修订 | Engineering specialist / 工程执行者 | Verify the changed behavior; keep lightweight workers on bounded tasks / 按变化的行为核验，轻量执行者承担边界清晰的小任务 |
| Small bounded feature / 规格明确的小功能 | DS 4.1 Flash max | Contract tests / 契约测试 |
| Implementation and repair / 常规实现与修复 | Sol 6.2 max | Independent reviewer with source and tests / 由实现外审查者核源码与测试 |
| Coupled backend systems / 复杂后端 | Astra 6.2 xhigh | One independent senior reviewer / 一位高难度独审 |
| Evidence-based review / 有依据的审查 | A coding specialist, or a senior orchestration mode for harder work / 编码专长模型，高难工作可选编排器 | Cite location, trigger and impact / 说明位置、触发条件和影响 |
| Visual UI and interaction / 前端视觉与交互 | Visual specialist, with a senior mode for complex work / 视觉专长模型，复杂任务可用高档模式 | Render the UI and verify state and data contracts / 查渲染、状态及数据合同 |
| Literature and dialogue / 文学与对白 | A single literary model / 单模型执笔 | Check the brief, voice and facts / 按设定、声音与事实核验 |

If the project owner enables rush mode, keep only basic tasks suited to DS on DS 4.1 Flash max. Route all other model execution and formal review to Astra 6.2 max in this configuration. Scripts and PMs keep their usual settings. Choose one reviewer outside the implementation team. A cluster that produced the implementation cannot provide its independent review. A manual handoff for exceptional design or review uses the same evidence and independence rules.

项目作者开启赶工后，适配 DS 的基础任务继续用 DS 4.1 Flash max，示例中其余模型执行与正式审查统一用 Astra 6.2 max。脚本和 PM 沿用原配置。每单正式审查由一位实现外审查者负责。已参与实现的集群只能自检。低频高难设计或审查可人工交接，回包按原合同验收。

## Reception / 接收

| PM type / 通道 | Example PM / 协调示例 | How it receives work results / 接收方式 |
| --- | --- | --- |
| Native GPT subagents | Terra 6.1 low | Direct parent receives supported events or waits in an active turn / 直接父会话在有效回合内接事件或等待 |
| Third-party subagents | DS 4.1 Flash high | Without reliable events, use bounded, low-frequency waits for known children / 无可靠事件时对已知子任务低频有界接收 |
| Agent Bridge | DS 4.1 Flash high | Pull known tasks for one bounded window per call. Process pause or new work before the next window / 每次拉取一个有界窗口，先处理暂停或插单再续收 |

For an orchestrator, select the exact ID from the installed CLI catalog. Start a fresh session and omit a separate effort field when the CLI does not support one. Record a bridge validation failure separately from a worker rejection; neither establishes the service’s effective effort.

编排器按已安装 CLI 的目录选精确 ID。当前端将多个选项合组时，仍以 CLI 可用的选择器为准。新开会话；CLI 不支持独立强度参数时省略该字段。分别记录派发前校验、worker 拒绝与服务端实际档位。

The controller receives substantive PM reports. Keep separate deadlines and resource ownership per task. Bind a mode with automatic effort by its host contract, omitting the effort field when required. Receipt of an output establishes delivery. Record internal model identity, cost and suitability only to the extent evidenced.

主控只收 PM 的实质回执。每单分别绑定截止和资源归属。自动强度模式按宿主合同省略相应字段。内部模型身份、成本、任务适用性分别以可核证据记载。见 [PM 接收合同 / Reception contract](../skills/forge-pm-management/references/reception.md)。
