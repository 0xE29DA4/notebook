# SSH

## SSH Config

PS: remember to reload ssh service after editing configuration

> user config in: `~/.ssh`

- id_rsa/id_ed25519: 私钥
- id_rsa_pub/id_ed25519.pub: 公钥
- authorized_keys: 存放公钥，允许这些公钥登录当前用户
- config: 用户级 SSH 客户端配置
- known_hosts: 记录了曾经连接过的 SSH 服务器的公钥指纹
- known_hosts.old: known_hosts 的备份

> systematic global config in: `/etc/ssh`

- ssh_config: 系统级 SSH 客户端配置
- sshd_config: SSH 服务端配置
- ssh_host_*_key: SSH 服务端私钥
- ssh_host_*_key.pub: SSH 服务端公钥

**ssh_config 常用配置项：**

```ssh_config
Host 配置名称
  HostName github.com                # 定义匹配的主机，可以使用通配符
  User user                          # 登录用户名
  Port 22                            # SSH 端口
  IdentityFile ~/.ssh/id_ed25519     # 使用的私钥文件
  ForwardAgent yes                   # 是否允许代理转发
  ProxyJump user@jump.example.com    # 设置跳板机服务器
  ServerAliveInterval 60             # 心跳间隔
  ServerAliveCountMax 5              # 服务端的 AliveCountMax
  StrictHostKeyChecking ask          # 严格检查服务器公钥
```

**sshd_config 常用配置项：**

```sshd_config
# 基础行为
Port 22                              # SSH 服务端监听端口
ListenAddress                        # SSH 服务端监听地址

# 认证相关
PermitRootLogin prohibit-password    # 登录 root 用户的配置
PermitEmptyPasswords no              # 是否允许空密码
PasswordAuthentication no            # 是否允许密码登录
PubkeyAuthentication yes             # 是否允许公钥认证登录
AllowUsers mizu                      # 允许登录的用户
AllowGroups admin                    # 允许登录的组
DenyUsers mizu                       # 禁止登录的用户
DenyGroups admin                     # 禁止登录的组
AuthorizedKeysFile                   # 指定 authorized_keys 路径
LoginGraceTime 2m                    # 登录宽限时间（用户在几秒内必须认证成功，默认 120s）
MaxAuthTries 3                       # 最大认证尝试次数

# 加密相关
HostKey                              # 指定服务器私钥文件路径
Ciphers                              # 指定可用的加密算法列表
MACs                                 # 指定消息认证码算法
KexAlgorithms                        # 指定密钥交换算法

# 会话相关
ClientAliveInterval 60               # 心跳间隔
ClientAliveCountMax 3                # 多少次无响应后断开连接

# X11/转发
X11Forwarding no                     # 允许 X11 转发
AllowTcpForwarding yes               # 是否允许端口转发
```

## 登录

```sh
# 使用私钥登录
ssh -i 私钥 USERNAME@IP
# 测试可登录性
ssh -i 私钥 USERNAME@IP -T
# 指定端口
ssh -p 2222 USERNAME@IP
# 使用跳板机
ssh -J JUMP_USER@JUMP_HOST TARGET_USER@TARGET_HOST
# 本地端口转发
ssh -L 7890:localhost:7890 mizu@192.168.1.100
# 远程端口转发
ssh -R 7890:localhost:7890 mizu@192.168.1.100
# 后台执行命令
ssh mizu@192.168.1.100 'nohup myscript.sh &'
```

## 密钥

### ssh-keygen

```sh
# 生成一个密钥对
# -t: 使用 ed25519 算法生成密钥
# -C: 为密钥对添加注释
ssh-keygen -t ed25519 -C "comment"
# 清除某个主机的密钥
ssh-keygen -R HOST
```

### ssh-copy-id

> 将公钥上传到服务器，它会自动完成所有必要步骤，包括在服务器上创建 ~/.ssh 目录、设置正确的文件权限以及将公钥追加到 authorized_keys 中

```sh
ssh-copy-id USERNAME@IP
# 如果公钥不是默认名称或默认路径，需要指定路径
ssh-copy-id -i 公钥路径 USERNAME@IP
```

## scp

> 使用 ssh 传输文件

```sh
# 将本地文件复制到远程
scp LOCALPATH USERNAME@IP:REMOTEPATH
# 将远程文件复制到本地
scp USERNAME@IP:REMOTEPATH LOCALPATH
```
