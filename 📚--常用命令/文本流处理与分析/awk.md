# awk

> 强大的文本处理工具，用于模式扫描和处理语言。

- 打印每行的第 1、3 列
  ```shell
  awk '{ print $1, $3 }' file.txt
  ```

- 指定分隔符为 ':'
  ```shell
  awk -F ":" '{ print $1 }' file.txt
  ```

- 打印包含 error 的行
  ```shell
  awk 'error { print }' file.txt
  ```

- 打印第 3 列大于 100 的行
  ```shell
  awk '$3 > 100 { print }' data.txt
  ```
