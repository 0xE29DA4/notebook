# nix run

> 不进入 Shell，直接构建并运行包中的默认可执行程序。

### 常用用法

- **运行 nixpkgs 中的包**
  ```shell
  nix run nixpkgs#hello
  ```

- **运行特定版本的包**
  ```shell
  nix run github:nixos/nixpkgs/nixos-24.11#cowsay -- "Hello Nix!"
  ```

- **运行当前 Flake 定义的 defaultPackage**
  ```shell
  nix run .
  ```

### 与 `nix shell` 的区别
- `nix shell`：将包放入环境变量并进入交互式 Shell。
- `nix run`：直接定位包中的可执行文件并执行，运行结束后不保留环境痕迹。

> [!TIP]
> 它是测试某个工具（如 `cowsay`, `figlet` 等）最快的方式，完全不污染当前环境。
