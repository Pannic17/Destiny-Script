# Destiny-Script

本仓库包含原有 Python 脚本，以及从 [P-D2](https://github.com/Pannic17/P-D2) 迁入的 JSON 配置。

## 目录

- 根目录：原有的 `buy.py`、`gta.py`、`main.py`、`pvp.py`、`script.py`，此次迁移未修改这些脚本。
- `json/`：P-D2 原仓库的全部 11 个受 Git 跟踪的文件，包括 5 个 JSON 文件、`.gitattributes` 和原有 `.idea/` 配置。

JSON 配置路径：

```text
json/PanNic.json
json/PanNic-Wishlist.json
json/PanNic-S25.json
json/PanNic-S25-1.json
json/PanNic-S25-2.json
```

## 迁移记录

2026-10-08 使用 Git subtree 将 P-D2 的 `main` 分支导入 `json/`，没有压缩历史；原仓库全部 9 条提交保留在本仓库提交图中。

- P-D2 来源提交：`0243d64b3dc3f4aef066ac816fa0ef897bb8a9f0`。
- Destiny-Script 迁移前提交：`b561f17624a60e287b1a5274a3fe3dbc9c757e86`。
- 迁入文件逐字节校验通过，导入时 `json/` 的 Git 文件树与 P-D2 来源提交的文件树完全一致。
- 5 个 JSON 文件均通过 JSON 解析检查。

历史可通过 `git log --all --graph --oneline` 查看。P-D2 原提交中的路径仍为当时的根目录路径；从导入提交起，文件位于 `json/` 下。

迁移只涉及文件与 Git 历史。使用旧仓库地址的外部工具或收藏链接，需要改为本仓库的 `json/` 路径；GitHub 不会自动重定向删除后的 P-D2 链接。

## 本地备份与恢复

迁移时另外生成了完整 Git 备份 `E:\Projects\Destiny2\P-D2-backup.bundle`，它位于两个仓库目录之外，未上传到本仓库。可以独立恢复原仓库：

```powershell
git clone E:\Projects\Destiny2\P-D2-backup.bundle E:\Projects\Destiny2\P-D2-restored
```

确认远端迁移内容后，可删除原 P-D2 仓库；建议保留上述 bundle 作为额外恢复副本。
