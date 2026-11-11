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

For managed client deployments, include `work-dispatch` and its runtime, work-order and attribution references in the baseline, with pointers to that project's governance. Preserve valid local customizations. Record gaps for completion under existing authorization; do not mark the baseline installed until required files are present and their references resolve. Client membership is selected for each rollout. The optional [model-selection note](WORK-DISPATCH-MODELS.md) remains separate from skill instructions.

纳管客户的技能基线包含派工技能、运行/工单/归属引用及项目治理入口；保留有效定制，缺项按既有授权补齐前保持未完成，必需文件齐备且引用可达后才记为标配安装完成。客户名单按每轮选择。模型选型说明独立存放，不进入 Skill。

可在脱离维护仓库的目录中重建同字节 ZIP。核对可信发行渠道的摘要后再接受包身份；目录和归档通过静态核验并不证明宿主或业务验收。
