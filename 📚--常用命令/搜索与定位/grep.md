# grep

> Global Regular Expression Print，全局正则表达式打印。

- 在文件中搜索字符串
  ```shell
  grep "search_term" file.txt
  ```

- 递归搜索目录
  ```shell
  grep -r "search_term" .
  ```

- 忽略大小写
  ```shell
  grep -i "search_term" file.txt
  ```

- 反向匹配 (显示不包含的行)
  ```shell
  grep -v "search_term" file.txt
  ```
