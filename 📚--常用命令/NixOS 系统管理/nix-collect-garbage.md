# nix-collect-garbage

> 垃圾回收工具，删除未被使用的 store 路径以释放空间。

- **删除超过 30 天的旧生成**
  ```shell
  sudo nix-collect-garbage --delete-older-than 30d
  ```

- **激进清理 (删除所有历史生成，仅保留当前)**
  ```shell
  sudo nix-collect-garbage -d
  ```

- **硬链接优化 (去重)**
  ```shell
  nix-store --optimise
  ```

---

### 现代推荐方案: `nh clean`

如果你安装了 [nh](nh.md)，可以使用更平衡的清理策略：

- **根据保留生成的数量清理**
  ```shell
  nh clean all --keep 5
  ```
