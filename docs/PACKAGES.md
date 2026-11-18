# Public source bundle / 公共源码包

Use Python 3.10 or later and the [standalone tool](../scripts/public_package.py). It requires no Git history, account, credentials, private tree or network. Run it in a clean release tree; a root Git metadata entry is ignored without traversing it. Other extra files, empty directories, symlinks and reparse points are rejected.

From the unpacked source root, verify the directory and recreate the deterministic ZIP in its parent:

```bash
python scripts/public_package.py verify .
python scripts/public_package.py build . ../skill-forge-public.zip
python scripts/public_package.py verify ../skill-forge-public.zip
```

For an original Release ZIP, optionally pass `--zip-sha256` or `--tree-sha256` with the expected digest from a trusted release channel. The Git provider's automatically produced source archive is not the canonical ZIP. The public manifest lists each payload file's path, size and SHA-256. Its tree digest binds that exact inventory; the ZIP uses a fixed member order, timestamp and permissions. The manifest excludes itself from the inventory. A modified manifest and payload are not independently authenticated without a trusted digest or another trusted distribution mechanism.

The release identity is product version plus public revision. The bundle contains one public source tree, its public manifest, AGPL and upstream MIT text, and no customer payload. The standalone tool verifies bytes; it does not deploy files, change host settings, or certify skill behavior.

For a full installation, include the `pm-management` and `work-dispatch` skill directories with their references and keep their relative links valid. Use pointers to the adopting project's own governance. Preserve valid local customizations. For an incremental installation, verify the agreed files and links. A project with an established PM initialization and reception contract may point dispatch to that contract through its local reference. Client membership is selected for each rollout. The optional [model-selection note](WORK-DISPATCH-MODELS.md) remains separate from skill instructions.

完整安装同时交付 `pm-management` 与 `work-dispatch` 两个技能目录，保留各自正文和全部引用，核对跨技能相对链接及项目自己的治理入口。增量安装按本轮范围核收文件及引用。客户已有 PM 初始化和接收合同的，可由派工技能经本地短指针接入。纳管客户按各轮范围选择；[模型选型说明](WORK-DISPATCH-MODELS.md)独立于技能。

可在脱离维护仓库的目录中重建同字节 ZIP。核对可信发行渠道的摘要后再接受包身份；目录和归档通过静态核验并不证明宿主或业务验收。
