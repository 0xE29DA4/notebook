# sed

> Stream Editor，强大的流式文本编辑器，常用于替换、删除、新增文件内容。

- 替换文本中的字符串 (输出到 stdout)
  ```shell
  sed 's/old/new/g' file.txt
  ```

- 直接修改文件内容
  ```shell
  sed -i 's/old/new/g' file.txt
  ```

- 删除第 3 行
  ```shell
  sed '3d' file.txt
  ```
