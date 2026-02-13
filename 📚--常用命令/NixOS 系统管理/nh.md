# nh (Nix Helper)

> Yet another Nix Helper. 旨在为 NixOS 用户提供更加符合习惯、更简洁的命令行体验。

### 核心功能

- **系统切换 (OS Switch)**
  ```shell
  nh os switch .
  ```
  *(注：会自动寻找当前目录下的 flake.nix，并根据当前 hostname 进行构建)*

- **垃圾回收 (Clean)**
  ```shell
  # 保留最近 5 个生成，清理其余内容
  nh clean all --keep 5
  ```

- **包搜索 (Search)**
  ```shell
  nh search firefox
  ```

- **输入更新 (Update)**
  ```shell
  nh os switch . --update
  ```

### 为什么使用 nh?
1. **语法简洁**：不再需要记忆冗长的 `nixos-rebuild` 参数。
2. **可视化输出**：默认模拟 `nix-output-monitor` 的日志展示。
3. **安全清理**：比原生的 `nix-collect-garbage` 更智能的保留策略。
