# nixos-option

> 在命令行中查询 NixOS 配置选项的状态及其定义位置。

### 常用用法

- **查询某个选项的当前值及其默认值**
  ```shell
  nixos-option boot.loader.grub.enable
  ```

- **查询包含子选项的配置组**
  ```shell
  nixos-option networking
  ```

### 现代替代方案: `nix-inspect` 或交互式探索
虽 `nixos-option` 依然可用，但许多用户现在更倾向于使用编辑器插件（如 `nixd` 或 `nil` LSP）来直接在代码中跳转定义。

如果你想通过命令行检查 Flake 中的配置，有时需要指定：
```shell
# 这种用法较复杂，取决于具体的 flake 结构
nix eval .#nixosConfigurations.<hostname>.options.services.nginx.enable
```
