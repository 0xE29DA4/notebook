# nix-store

> 操作 Nix Store。

- 验证 Store 完整性
  ```shell
  nix-store --verify --check-contents
  ```

- 优化 Store (硬链接去重)
  ```shell
  nix-store --optimise
  ```
