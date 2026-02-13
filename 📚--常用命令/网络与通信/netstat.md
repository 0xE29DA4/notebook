# netstat

> 打印网络连接、路由表、接口统计信息 (建议使用 ss 代替)。

- 显示所有监听端口 (TCP/UDP)
  ```shell
  netstat -tuln
  ```

- 显示拥有者进程
  ```shell
  sudo netstat -tulnp
  ```
