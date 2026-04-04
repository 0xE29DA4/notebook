# ssh-keygen

```sh
# 生成一个密钥对
ssh-keygen -t ed25519 -C "COMMENT"
# 清除某个主机的密钥
ssh-keygen -R HOST
# 计算密钥指纹
ssh-keygen -l -E sha256 -f ~/.ssh/id_ed25519.pub
```
