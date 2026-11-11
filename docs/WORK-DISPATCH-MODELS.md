# Model routing and PM roles / 派工模型与双 PM

Read this note when choosing or revising a project's routes. It stays outside skills and their references; agents do not need it for every assignment. The model labels below describe a reference setup. Resolve available model IDs and effort levels in your own host, and keep your project's approved routes authoritative. A native-only setup uses the GPT route; third-party routing is optional.

本文供主控选型或修订路由时按需阅读，放在 Skill 及其 references 之外，不随每单加载。以下模型名称属于参考组合，实际标识和档位以目标宿主可用项为准；项目已确认路由优先。纯原生环境只采用 GPT 路线，第三方适配可选。

## Executors / 执行者

| Work / 工作特性 | Example model and effort / 参考选档 | Boundary / 适用边界 |
| --- | --- | --- |
| Small, fully specified features and mechanical checks / 低难度、规格明确的小功能及机械核验 | DS 4.1 Flash / `max` | Fixed UI bindings, field mapping, local adapters and contract tests; return unspecified cross-system transactions, save compatibility or major performance decisions to the controller / 既定 UI 绑定、字段映射、局部适配及明确契约测试；未约定的跨系统事务、存档兼容或重大性能取舍交回主控 |
| Bounded implementation, test design and independent review / 边界明确的中档实现、测试设计及独立审查 | Sol 6.1 / `max` | Correctness, maintainability, state machines and resource lifecycles / 正确性、可维护性、状态机和资源生命周期 |
| Complex judgment, implementation and repairs / 复杂判断、中高难度实现与修复 | Sol 6.1 / `max` | Judge fit from the actual task and delivery / 按本单判断量及交付结果选用 |
| Coupled contracts, major correctness risk and difficult cross-system work / 多系统合同耦合、重大正确性风险与难拆解攻坚 | Astra 6 / `xhigh` | May be selected directly when the risk warrants it / 风险明确时可直接选用，无需先让 Sol 失败 |
| Proven mechanical procedures / 已验证的机械流程 | Script first; Terra 6.1 / `low` if an agent is needed / 优先脚本，确需代理时用 Terra | Fixed entry points, collection and closeout; return open-ended diagnosis or unresolved cross-domain design to the controller / 固定入口、采集与收口；开放诊断或未定跨域设计交回主控 |

The controller owns escalation. Rule out tool, permission, environment and scope problems before attributing a failure to model capability. A real semantic bottleneck or repeated rework can justify Astra/xhigh; higher Astra efforts require explicit project-owner approval. PMs do not change providers or increase effort on their own. Independent review uses someone who did not implement the change.

主控决定升档，先排除工具、权限、环境和范围问题。存在实质语义瓶颈或同类返工时可评估升至 Astra/xhigh，更高 Astra 档位须经项目作者明确批准；PM 不自行换供应商或升档。独立审查由未参与实现者承担。

## Coordinating PMs / 协调 PM

| Route / 路线 | PM model and effort / PM 选档 |
| --- | --- |
| GPT family / GPT 家族 | Terra 6.1 / `low` |
| Optional third-party family / 可选第三方模型 | DS 4.1 Flash / `high` |

PMs repeatedly dispatch, wait and collect results, so this example balances cost, required judgment and model-family compatibility. Split the two PMs by family or runtime route; either can coordinate implementation or independent review. The split does not itself establish independence or runtime compatibility; see the [runtime contract](RUNTIME-CONTRACT.md).

PM 反复经历派工、等待和回收，因此这套选型兼顾经济性、所需智能与模型家族兼容性。双 PM 按家族或运行通道分工，两者都可派实现或独立审查；角色划分本身不证明审查独立性或通道兼容性，见[运行约定](RUNTIME-CONTRACT.md)。

PMs dispatch frozen work and collect events, checking only essential completeness. Controllers retain engineering decisions and acceptance; open-ended diagnosis and business review belong to appropriate specialists. Each child task explicitly selects its own model and effort. Use completion events rather than polling to keep a coordinator alive. These choices are a starting point, not measured cost or performance results.

PM 只负责冻结派工、事件回收和最低完整性检查；工程裁决与验收归主控，开放诊断及业务审查交相应专业执行者。子任务显式选择自己的模型与档位，不继承 PM 设置。采用完成事件回收，不轮询保活；本表不构成本轮费用或性能实测。
