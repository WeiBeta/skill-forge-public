# Upgrade a shared kit / 升级共享工程套件

Freeze the current release and proposed upstream changes. Compare the exact baseline and target, record upstream attribution, and select changes by the adopting project's need. A newer revision is evidence of a source change; it does not establish compatibility or grant permission to apply it.

1. Inventory upstream, maintained core and project-owned customizations. Keep adoption decisions and source hashes; avoid overwriting downstream domain rules.
2. Produce one reviewable candidate. State what changed, why, target versions, owned paths and evidence that must be renewed.
3. Validate installation targets, links, license texts and exact package bytes. Use the smallest authorized check that can answer the question. Bind formal acceptance to the actual candidate and results; renew only evidence affected by a change.
4. Keep baseline, candidate and relevant before/after evidence. Stage deployment under the target owner's scope and preserve [recovery records](DEPLOYMENT-RECOVERY.md).

候选生成、独立审查、部署、加载、效果验证分别登记。仅作评估时，交付差额和建议；用户没有授予实施时不改目标实例。
