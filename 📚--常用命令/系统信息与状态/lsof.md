# lsof

> List Open Files，列出打开的文件和相应的进程。注意：列出其他人打开的文件需要 root 权限。

- 查看端口占用情况
  ```shell
  lsof -i tcp:3306
  ```

- 查看指定用户打开的文件
  ```shell
  lsof -u username
  ```

- 查看指定文件被哪个进程占用
  ```shell
  lsof /path/to/file
  ```
