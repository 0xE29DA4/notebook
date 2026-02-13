# nc

> Netcat，网络工具中的瑞士军刀。

- 监听端口 (作为服务器)
  ```shell
  nc -l 8080
  ```

- 连接端口 (作为客户端)
  ```shell
  nc host 8080
  ```

- 端口扫描
  ```shell
  nc -zv host 20-80
  ```
