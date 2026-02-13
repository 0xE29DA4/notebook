# nix-health

> NixOS 系统的快捷体检工具。

### 使用方法

- **运行全方位检查**
  ```shell
  nix-health
  ```

### 检查项目
- **Nix 设置**：检查 `experimental-features` 是否包含 `flakes` 和 `nix-command`。
- **Store 权限**：检查 `/nix/store` 是否正常。
- **代理解析**：检查二进制缓存服务器的可达性。
- **系统状态**：检查是否在 NixOS 上运行。

> [!NOTE]
> 当你遇到 "明明配置了 Flake 还是报错" 或构建过程中出现诡异错误时，首先运行 `nix-health`。
