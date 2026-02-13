# cut

> 从文件的每一行中截取部分内容。

- 截取第 1 个字段 (默认按 tab 分隔)
  ```shell
  cut -f 1 file.txt
  ```

- 指定分隔符为 ":" 并截取第 1 和 3 个字段
  ```shell
  cut -d ":" -f 1,3 /etc/passwd
  ```

- 截取第 1 到 10 个字符
  ```shell
  cut -c 1-10 file.txt
  ```
