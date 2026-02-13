# tr

> Translate，转换或删除字符 (只能从标准输入读取)。

- 将小写转换为大写
  ```shell
  echo "hello" | tr 'a-z' 'A-Z'
  ```

- 删除所有数字
  ```shell
  echo "hello 123" | tr -d '0-9'
  ```

- 压缩重复字符 (如多个空格变一个)
  ```shell
  echo "hello    world" | tr -s ' '
  ```
