# ssh-keyscan

```sh
# 扫描主机公钥
ssh-keyscan HOST
# 扫描多个主机（逗号分隔或空格）
ssh-keyscan 100.111.111.11 vpn.chamomile.icu example.com
# 扫描并追加到 known_hosts
ssh-keyscan HOST >> ~/.ssh/known_hosts
```
