# Example: review a small parser change

Synthetic scenario. The project has a function that accepts status values `ready` and `held`. The candidate should reject a missing status while keeping both valid cases unchanged.

- Input: one named baseline and candidate, with the parser contract fixed before review.
- Executor: allowed to edit only the parser and its contract tests. Run local tests for the three behaviors; no remote calls.
- Acceptance: distinguish the intended rejection from any new failure on an existing valid input.
- Handoff: give the exact candidate, test result and any untested path. If independent review is required, bind a separate reviewer to those fixed inputs without write access.

If the test harness cannot load, record the failure and the intended test as unexecuted. Do not infer success from a tool's acceptance or increase retries without checking the cause.
