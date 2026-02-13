# nix-index / nix-locate

> Nix 的本地索引工具，用于快速查找文件所属的包。

### 核心用法

- **更新索引数据库 (初次使用必须)**
  ```shell
  nix-index
  ```
  *(注：这会下载一个几百 MB 的数据库，建议定期更新)*

- **查找包含特定文件的包**
  ```shell
  # 查找哪个包提供了 libfoo.so
  nix-locate libfoo.so
  ```

- **只查找 binary 文件**
  ```shell
  nix-locate --bin --type f hello
  ```

### 进阶建议
可以将 `nix-index` 的 `command-not-found` 钩子集成到 Shell 中：
- **Bash/Zsh**: 在配置中加入 `programs.nix-index.enable = true;` (通过 Home Manager 或 NixOS)。
- 之后当你输入一个未安装的命令时，系统会自动提示你：`The program 'xxx' is currently not installed. It is provided by...`
