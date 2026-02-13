# seq

> 打印数字序列。

- 生成 1 到 10 的序列
  ```shell
  seq 10
  ```

- 指定分隔符
  ```shell
  seq -s ":" 10
  # 输出: 1:2:3:4:5:6:7:8:9:10
  ```

- 指定范围和步长
  ```shell
  # seq [First] [Increment] [Last]
  seq 1 2 10
  # 输出: 1 3 5 7 9
  ```
