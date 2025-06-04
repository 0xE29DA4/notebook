# SSH

## 安装

```sh
# 安装 openssh
paru -S openssh
# 查看 ssh 版本
ssh -V
# 测试连接
ssh -i 私钥 -T USER@IP
```

## ssh 配置

> 在 ~ 下存在 .ssh 目录  
> 在 /etc 下存在 ssh 目录  
> 修改完配置后需要重启 ssh 服务

**ssh 配置文件：**

- ssh_config
  - ssh 客户端配置
- sshd_config
  - ssh 服务端配置
- known_hosts
  - 存放已知的主机
- autherized_keys
  - 存放公钥的文本

**ssh_config 常用配置项：**

```ssh_config
Host 主机名
  HostName 主机地址
  User 用户名
```

**sshd_config 常用配置项：**

```sshd_config
# 监听 22 端口
Port 22
# 允许密钥对登录
PubkeyAuthentication yes
# 禁用密码登录
PasswordAuthentication no
```

## 密钥对

### 生成密钥对

```sh
cd ~/.ssh
# -t: 指定使用安全的 ed25519 算法
# -C: 为密钥对添加注释
ssh-keygen -t ed25519 -C "注释"
# 会提问文件的保存路径，完全一样将覆盖先前的密钥对，passphrase 相当于二次密码校验，置空即可
# 完成后将生成两个文件，pub 文件是公钥，另一个是私钥
```

### 使用私钥登陆

```sh
ssh -i 私钥 USERNAME@IP
```

### 将公钥发送到服务端

```sh
ssh-copy-id -i 公钥路径 USERNAME_IP
```

### 清除某个主机的密钥

```sh
ssh-keygen -R IP_OR_HOSTNAME
```
