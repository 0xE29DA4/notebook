# nix-output-monitor (nom)

> 为 Nix 构建过程提供更清晰、更美观的终端输出。

### 使用方法

- **基础用法**
  只需将 `nix` 命令替换为 `nom` 即可（几乎所有 `nix` 命令都支持）：
  ```shell
  nom build .#hello
  nom shell nixpkgs#python3
  ```

- **配合 nixos-rebuild 使用**
  ```shell
  nixos-rebuild build --flake .#myhost |& nom
  ```

### 特点
- **实时进度条**：显示当前正在构建的包。
- **依赖树视图**：清晰展示并行构建的依赖关系。
- **错误高亮**：构建失败时更快速定位到错误行。
