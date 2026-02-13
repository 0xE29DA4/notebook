# find

> 在目录层次结构中搜索文件。

- 按名称搜索
  ```shell
  find . -name "*.txt"
  ```

- 按名称搜索 (忽略大小写)
  ```shell
  find . -iname "readMe.md"
  ```

- 按类型搜索 (f:文件, d:目录)
  ```shell
  find . -type d
  ```

- 搜索大于 100M 的文件
  ```shell
  find . -size +100M
  ```

- 对搜索结果执行命令
  ```shell
  find . -name "*.log" -exec rm {} \;
  ```
