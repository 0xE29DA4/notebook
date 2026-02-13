# systemctl

> Systemd 系统和服务管理器。

- 启动/停止/重启服务
  ```shell
  sudo systemctl start nginx
  sudo systemctl stop nginx
  sudo systemctl restart nginx
  ```

- 设置开机自启
  ```shell
  sudo systemctl enable nginx
  ```

- 查看服务状态
  ```shell
  systemctl status nginx
  ```
