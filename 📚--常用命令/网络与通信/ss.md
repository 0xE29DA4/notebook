# ss

> Socket Statistics，转储套接字统计信息 (比 netstat 更快更详细)。

- 显示所有监听的 TCP/UDP 端口
  ```shell
  ss -tuln
  ```

- 显示连接的进程信息
  ```shell
  sudo ss -tulnp
  ```
