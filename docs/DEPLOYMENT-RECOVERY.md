# Deploy and recover / 部署与恢复

Bind the exact target instance, allowed paths, package identity, expected current state and acceptable rollback before touching a target. Cloning or building a package does not deploy it.

| Record | Preserve |
| --- | --- |
| Before | Actual target bytes or explicit absence for each allowed path, source identity, authorized scope and drift |
| Candidate | Input release and file SHA-256, exact add/change/remove operations, validation and known gaps |
| After | Observed bytes, applied/failed/unknown operations, validation and any follow-up needed |
| Before rollback | Current target and intervening changes; record the new authorization and restore scope |

Check drift against the fixed expectation and retain unexplained changes. Never overwrite a changed instance on the strength of a matching filename. Keep originals, failure evidence and recovery materials separate from the source repository; restrict access according to their contents. Backups and their hashes prove possession, not recoverability.

Apply only approved changes. Verify actual target paths and raw bytes afterwards. Track file placement, host discovery, load, use, business acceptance and recovery rehearsal separately. A failed or interrupted operation may have side effects; observe them before retrying. For rollback, restore only the bound difference and verify the resulting target, preserving intervening changes outside that scope.

回滚范围、保留条件和删除权限分别决定。样例不授予操作权限，也不宣称恢复已经演练。升级决策见[升级指南](UPGRADE.md)。
