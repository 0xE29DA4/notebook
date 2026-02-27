# ssh-copy-id

> 将公钥上传到服务器，它会自动完成所有必要步骤，包括在服务器上创建 ~/.ssh 目录、设置正确的文件权限以及将公钥追加到 authorized_keys 中

```sh
ssh-copy-id USER@IP
# 如果公钥不是默认名称或默认路径，需要指定路径
ssh-copy-id -i 公钥路径 USER@IP
```
