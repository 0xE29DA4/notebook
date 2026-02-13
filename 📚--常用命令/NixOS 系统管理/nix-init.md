# nix-init

> 自动生成 Nix 包定义的交互式工具。

### 使用方法

- **从 GitHub URL 创建包定义**
  ```shell
  nix-init https://github.com/username/repo
  ```

### 特点
- **自动检测构建系统**：自动识别 Rust (Cargo), Python (Poetry/Setuptools), Go 等。
- **自动抓取 Hash**：无需手动运行 `nix-prefetch-url`。
- **补全元数据**：自动填充 `description`, `license`, `homepage` 等字段。

> [!TIP]
> 它是 Nix 开发者/包维护者最常用的生产力工具。
