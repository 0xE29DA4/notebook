# kill

> 向进程发送信号 (通常用于终止进程)。

- 终止进程 (默认发送 SIGTERM)
  ```shell
  kill <PID>
  ```

- 强制终止进程 (SIGKILL)
  ```shell
  kill -9 <PID>
  ```

- 列出所有信号
  ```shell
  kill -l
  ```
