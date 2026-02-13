# nix-tree

> 基于终端的交互式 Nix Store 依赖树浏览器。

### 使用方法

- **浏览当前系统中某个包的依赖**
  ```shell
  nix-tree /nix/store/xxxxxx-my-package
  ```

- **浏览某个 Flake 输出的结果**
  ```shell
  nix-tree .#packages.x86_64-linux.default
  ```

### 交互快捷键
- `j / k`: 上下移动。
- `h / l`: 展开/收起依赖项。
- `i`: 显示当前路径的信息 (Size, Referring paths)。
- `/`: 搜索。
- `q`: 退出。

### 适用场景
- 分析为什么某个 derivation 体积巨大。
- 确认某个特定的补丁或库版本是否被正确引入依赖。
