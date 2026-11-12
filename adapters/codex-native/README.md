# 路线 A：原生 Codex

使用 Codex 原生模型、子代理和自定义角色。先在目标版本确认实际工具面与配置字段。工作区写入、请求审批和角色定义仅作最小示例；本版未执行宿主、等待、关闭或业务验收。

- [config.example.toml](config.example.toml) 示范工作区写入、审批和并发上限。按需合并核过的最小差额，不覆盖用户现行配置。
- [rules.example.rules](rules.example.rules) 仅演示命令规则。若目标核心支持，先用规则检查功能验证；不要实际执行破坏性命令作为测试。
- [reviewer.toml](agents/reviewer.toml) 绑定角色说明。角色文本不建立新的沙箱，读取的角色细则来自采用方按[治理范本](../../templates/project/AGENTS.md)裁剪后的项目。

官方入口：[子代理和自定义角色](https://learn.chatgpt.com/docs/agent-configuration/subagents)、[自动审批审查](https://learn.chatgpt.com/docs/sandboxing/auto-review)。不要把可选路线的实验等待字段带入原生配置；当前实际工具能力优先。

接入时先验证一次可逆任务：工具受理、角色的实际写入范围、等待或回执、资源关闭。详细的已知与未测边界见[验收指南](../../docs/VALIDATION.md)。


## 直接父会话的等待边界

直接父会话（含获准直派的主控）在回合内消费原生子任务结果；主控等待独立PM的消息另走结束与续接路径，见[运行适配](../../skills/forge-work-dispatch/references/runtime.md#三条接收路径)。采用方应以实际工具族与生命周期证据选择分支，不凭模型家族保证V1/V2，更不把回合内挂起返回当作已结束父回合自动唤醒。

无适用事件的通道只使用项目明确授权的有界等待/必要精确确认。所有等待路径均在适用预算耗尽或无合法调用区间时保存未终态、已用预算与恢复入口，同时停止追加等待/确认，不续额、不重派、不取消业务。工具schema与上层限制同时约束调用，历史等待参数不是豁免。此参考不安装配置、不启动模型验证，也不授权高价主控轮询。
