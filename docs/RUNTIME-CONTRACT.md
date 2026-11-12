# Runtime contract / 运行合同

Discover capabilities from the actual installed tool surface. A configured feature or adapter file does not prove its behavior.

| Capability | Evidence to distinguish |
| --- | --- |
| Dispatch | Requested parameters, tool acceptance, self-report and actual routing evidence |
| Isolation | Resolved work root, actual read/write policy, shared Git metadata and exclusive resources |
| Completion | Tool event, substantive response, checked result and the parent's acceptance |
| Wait and resume | Active-parent wait, independent-session handoff, timeout and pause |
| Closure | Execution terminal state, close operation and resource release |
| Recovery | Authorization, observed side effects, remaining budget and verified restoration |

Use the event or handoff mechanism the target supports. Missing events may require user continuation; polling, empty acknowledgements and speculative wake-ups do not establish a reliable event contract. Do not treat a wrapper timeout as proof that a business action did not occur. An unreported underlying model or resource state stays `Unknown`.

V1 and V2 are names used by some host versions; do not assume equivalent parameters or lifecycle. See the [native](../adapters/codex-native/README.md) and [optional](../adapters/opencodex/README.md) route boundaries and the [validation guide](VALIDATION.md).


## 等待采用入口

主控只等独立PM时按已验证消息机制结束；直接父会话（含获准直派的主控）仍须回收子任务时保持接收回合，用实际事件/直接等待。没有适用事件时，只沿项目明确授权的有界等待与必要精确确认；无授权则交接人工续接。所有等待路径都在适用预算耗尽或schema与上层限制无合法交集时保存非终态、已用预算和恢复入口，同时停止追加等待/确认，不自行续额、重派或取消业务。这里的适配不是列表轮询、空ACK或定时保活许可，也不证明已结束父回合会被自动唤醒。

首次采用或出现误用时查[三条接收路径](../skills/forge-work-dispatch/references/runtime.md#三条接收路径)，之后复用已有能力证据。
