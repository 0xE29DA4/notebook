# scp

> Secure Copy，通过 SSH 在主机间安全复制文件。

- 复制文件到远程主机
  ```shell
  scp file.txt user@host:/path/to/remote
  ```

- 从远程主机复制文件
  ```shell
  scp user@host:/path/to/remote/file.txt .
  ```

- 递归复制目录
  ```shell
  scp -r directory user@host:/path/to/remote
  ```
