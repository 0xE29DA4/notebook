# frp

- 需要一台公网服务器
- 以下称两台处于不同局域网的主机分别为 A、B
- client(A、B) 使用 frpc，server 使用 frps

#  Server 端

## 启动服务

```shell
# 在 frp 目录下
./frps -c ./frps.ini
```

# Client 端

## 启动服务

```shell
# 在 frp 目录下
./frpc -c ./frpc.ini
```

# A 访问 B

```shell
ssh -p <frp设置的remote_port> user@ip
```

# 配置 frp 自启动

## frps

```shell
# frp 下带有 systemd 文件夹
# 拷贝 frps.service 中的内容

cd /lib/systemd/system
sudo vim frps.service # 需要改动 User 和 ExecStart

# 启动 frps
systemctl daemon-reload
systemctl enable frps
systemctl start frps
```

## frpc

```shell
```