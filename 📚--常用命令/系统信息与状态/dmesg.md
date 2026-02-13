# dmesg

> Diagnostic Message，显示内核环形缓冲区的信息 (通常用于硬件故障诊断)。

- 显示所有内核消息
  ```shell
  dmesg
  ```

- 搜索包含 error 的消息
  ```shell
  dmesg | grep -i error
  ```

- 以人类可读的时间戳显示
  ```shell
  dmesg -T
  ```
