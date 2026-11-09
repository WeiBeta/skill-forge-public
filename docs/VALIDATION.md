# Validation / 验收

Verify the smallest evidence that answers the question. The [public package tool](PACKAGES.md) checks file and ZIP integrity. It cannot establish host compatibility, successful routing, lack of idle requests, actual speedup, correctness of advice, or recoverability.

| Check | What to record | Public release boundary |
| --- | --- | --- |
| Package | Manifest, exact bytes and deterministic rebuild | Static; inspect the Release digest for your artifact |
| Discovery and load | Harness version, actual path, presence and load result | NotRun |
| Native lifecycle | Effective tool schema, authorized reversible task, wait and close evidence | NotRun |
| Optional third-party route | Version, protocol, actual routing evidence, timeout and close | NotRun |
| Business behavior and recovery | Expected result, actual result, failure evidence and restoration check | NotRun |

A sample that proves one combination does not prove another. Keep `NotRun` for work never executed and `Unknown` for an outcome without evidence. Record failed attempts separately, even if a later candidate passes.
