# Permissions / 权限

Authority for a change comes from the task and target owner. The ability to call a tool, a writable workspace, a permissive setting, a role instruction and approval by the runtime are different facts.

1. Identify the actual workspace, sandbox, approval path and tool surface for the current action.
2. Bind the allowed read and write paths, external effects and resource budget. Narrow a request to the required change, or continue independent work if a dependency is denied.
3. Stop the denied action and record why. Changing wrappers, roles, models or providers does not turn a rejected action into an authorized one.

The [native sample](../adapters/codex-native/config.example.toml) only illustrates a possible configuration. Do not overwrite unrelated settings or apply it without checking the installed version and applicable authority. A child agent or independent session does not automatically inherit the intended policy or use a separate writable checkout.

实际调用时分别记录业务授权、沙箱和审批结果；配置存在不证明生效。秘密仅留在获准的环境，不复制到回执或样例。
