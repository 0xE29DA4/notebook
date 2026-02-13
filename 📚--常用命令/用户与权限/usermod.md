# usermod

> 修改用户账户。

- 将用户添加到 sudo 组 (附加组)
  ```shell
  sudo usermod -aG sudo username
  ```

- 修改用户的 Shell
  ```shell
  sudo usermod -s /bin/zsh username
  ```
