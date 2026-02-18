# Debian 使用手册

## 安装必要软件

```sh
sudo apt update && sudo apt upgrade -y
sudo apt install -y zip unzip wget curl git libnss3-tools mkcert htop neofetch iproute2 tldr tree fish
sudo apt install -y locales fonts-wqy-microhei fonts-wqy-zenhei
sudo apt install -y build-essential gcc python3 nodejs npm
sudo apt install -y podman podman-compose podman-docker
```

## 更改用户 SHELL

```sh
chsh -s /usr/bin/fish
```

## 安装 Bun

```sh
curl -fsSL https://bun.sh/install | bash

```

## 安装 UV

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 设置系统语言为简体中文

```sh
# 交互式配置 locale
# 选择 en_US.UTF-8 与 zh_CN.UTF-8
sudo dpkg-reconfigure locales
# 生成所需的 locale
sudo dpkg-reconfigure locales
# 更新用户级环境变量
echo 'export LANG=zh_CN.UTF-8' >> ~/.bashrc
echo 'export LC_ALL=zh_CN.UTF-8' >> ~/.bashrc
source ~/.bashrc
# 验证
locale
# 查看 data 命令的输出语言
date
```

## 创建本地 CA

```sh
mkcert -install
mkdir -p ~/certs/localhost && cd $_
mkcert localhost 127.0.0.1 ::1
```

## 配置 Podman 镜像加速

编辑 `/etc/containers/registries.conf` 文件，添加配置：

```conf
unqualified-search-registries = ["docker.io"]

[[registry]]
prefix = "docker.io"
location = "mirror.ccs.tencentyun.com"
```

## 安装 rust

```sh
# 交互式脚本
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## 安装 acme.sh

```sh
curl https://get.acme.sh | sh -s email=0xE29DA4@gmail.com
# 卸载 acme.sh
acme.sh --uninstall
```
