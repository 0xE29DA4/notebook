# nix-env (Legacy)

> [!WARNING]
> `nix-env` 是旧版包管理工具，不支持 Flakes。在现代 NixOS (21.05+) 中，推荐使用 `nix profile`。

### 旧版用法 (不推荐)

- 安装包
  ```shell
  nix-env -iA nixpkgs.hello
  ```

- 卸载包
  ```shell
  nix-env -e hello
  ```

- 列出已安装的包
  ```shell
  nix-env -q
  ```

---

### 现代替代方案: `nix profile`

- **安装包**
  ```shell
  nix profile install nixpkgs#hello
  ```

- **列出已安装内容**
  ```shell
  nix profile list
  ```

- **更新所有包**
  ```shell
  nix profile upgrade --all
  ```

- **卸载包**
  ```shell
  nix profile remove <index_or_id>
  ```
  *(注：使用 `nix profile list` 查看索引号)*
