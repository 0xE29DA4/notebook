# nix-diff

> 比较两个 Nix Store 路径或 Derivation 之间的差异。

### 使用方法

- **比较两个包的差异**
  ```shell
  nix-diff /nix/store/...-old-package /nix/store/...-new-package
  ```

- **比较当前系统与上一个版本的差异 (NixOS)**
  ```shell
  nix-diff /nix/var/nix/profiles/system-100-link /nix/var/nix/profiles/system-101-link
  ```

### 适用场景
- **为何体积增加了?**：显示新版本中新增的依赖。
- **为何配置没生效?**：查看生成的配置文件在 store 路径中的具体内容变更。
- **Debug 修补程序**：确认 patch 是否真正改变了输出。
