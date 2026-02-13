# read

> 从标准输入读取一行并将其拆分为字段赋给变量。

- 读取输入到变量
  ```shell
  read -p "请输入用户名: " username
  echo "你好, $username"
  ```

- 使用默认变量 $REPLY
  ```shell
  read -p "确认吗? "
  echo "你的回答是: $REPLY"
  ```

- 读取多个变量
  ```shell
  read -p "请输入两个数字: " num1 num2
  ```

- 设置超时时间
  ```shell
  # 60秒超时
  read -t 60 -p "请在60秒内输入: " var
  ```
