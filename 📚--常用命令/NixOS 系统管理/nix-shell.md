# nix-shell (Legacy)

> [!WARNING]
> `nix-shell` 是旧版临时环境工具。在 Flake 模式下，推荐使用 `nix shell`（用于临时运行包）或 `nix develop`（用于开发环境）。

### 旧版用法

- 进入包含 python3 的环境
  ```shell
  nix-shell -p python3
  ```

- 运行命令并退出
  ```shell
  nix-shell -p python3 --run "python3 script.py"
  ```

---

### 现代替代方案

#### 1. `nix shell` (临时使用包)
- 启动包含指定包的 shell
  ```shell
  nix shell nixpkgs#python3 nixpkgs#requests
  ```

#### 2. `nix develop` (进入项目开发环境)
- 使用当前目录的 `flake.nix` 中的 `devShell`
  ```shell
  nix develop
  ```

#### 3. `nix run` (不进入 shell 直接运行)
- 运行包中的默认程序
  ```shell
  nix run nixpkgs#hello
  ```
