# nix flake

> 管理 Nix Flakes 的核心命令。

- **更新所有输入并锁定**
  ```shell
  nix flake update
  ```

- **仅更新特定输入**
  ```shell
  nix flake lock --update-input <input_name>
  ```

- **检查 Flake 语法与构建**
  ```shell
  nix flake check
  ```

- **显示 Flake 的输出结构 (packages, nixosConfigurations 等)**
  ```shell
  nix flake show
  ```

- **初始化新 Flake**
  ```shell
  nix flake init -t github:nixos/templates#full
  ```

- **查看依赖图**
  ```shell
  nix flake info
  ```
