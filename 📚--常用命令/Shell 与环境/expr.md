# expr

> 表达式计算工具。

- 数值计算 (注意转义)
  ```shell
  expr 5 + 5
  expr 5 \* 5
  expr 10 \> 1
  ```

- 统计字符串长度
  ```shell
  expr length "hello world"
  ```

- 模式匹配
  ```shell
  # 统计串长度，如果不以 jpg 为后缀返回 0
  expr "image.jpg" : ".*\.jpg"
  ```
