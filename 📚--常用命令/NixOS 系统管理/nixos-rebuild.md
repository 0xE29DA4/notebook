# nixos-rebuild

> NixOS 系统重构工具，用于应用配置更改。

- **使用 Flake 应用配置 (推荐)**
  ```shell
  sudo nixos-rebuild switch --flake .#<hostname>
  ```

- **仅构建不切换 (测试配置)**
  ```shell
  sudo nixos-rebuild test --flake .#<hostname>
  ```

- **构建并设置作为下次启动项 (不立即切换)**
  ```shell
  sudo nixos-rebuild boot --flake .#<hostname>
  ```

---

### 现代替代方案: `nh os`

如果你启用了 [nh](nh.md) (Nix Helper)，可以使用更简洁的语法：

- **切换系统**
  ```shell
  nh os switch .
  ```
  *(它会自动寻找当前目录下的 flake 及其 hostname)*

- **更新并切换**
  ```shell
  nh os switch . --update
  ```
