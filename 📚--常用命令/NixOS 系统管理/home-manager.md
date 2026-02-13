# home-manager

> 针对用户个人环境的内容管理工具（Dotfiles 管理）。

### 常用命令

- **应用配置更改**
  ```shell
  home-manager switch --flake .#username
  ```

- **查看当前生成 (Generations)**
  ```shell
  home-manager generations
  ```

- **删除旧生成**
  ```shell
  home-manager expire-generations "-30 days"
  ```

- **切换到特定生成**
  ```shell
  # <id> 通过 generations 命令获取
  /nix/store/...-home-manager-generation/activate
  ```

### 现代方案
如果使用了 `nh`，也可以通过 `nh` 管理：
```shell
# 自动识别 flake 和用户
nh home switch .
```
