# strace

> 跟踪系统调用和信号。

- 跟踪命令的系统调用
  ```shell
  strace ls
  ```

- 跟踪正在运行的进程
  ```shell
  sudo strace -p <PID>
  ```

- 统计系统调用时间
  ```shell
  strace -c ls
  ```
