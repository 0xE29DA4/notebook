# journalctl

> 查看 Systemd 日志。

- 查看特定服务的日志
  ```shell
  journalctl -u nginx
  ```

- 实时查看日志 (跟随模式)
  ```shell
  journalctl -u nginx -f
  ```

- 查看本次启动后的日志
  ```shell
  journalctl -b
  ```
