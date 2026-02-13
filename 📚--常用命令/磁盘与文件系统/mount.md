# mount

> 挂载文件系统。

- 挂载设备到目录
  ```shell
  mount /dev/sda1 /mnt/usb
  ```

- 显示所有挂载点
  ```shell
  mount
  ```

- 重新挂载为读写模式
  ```shell
  mount -o remount,rw /
  ```
