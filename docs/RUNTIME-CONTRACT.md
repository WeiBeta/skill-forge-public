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
