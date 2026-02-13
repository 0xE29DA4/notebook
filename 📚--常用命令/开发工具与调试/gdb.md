# gdb

> GNU Debugger，程序调试工具。

- 调试可执行文件
  ```shell
  gdb ./a.out
  ```

- 常用命令
  - `run (r)`: 运行程序
  - `break (b) main`: 在 main 函数打断点
  - `next (n)`: 单步执行 (不进入函数)
  - `step (s)`: 单步执行 (进入函数)
  - `continue (c)`: 继续运行
  - `print (p) var`: 打印变量
  - `bt`: 查看调用栈
  - `q`: 退出
