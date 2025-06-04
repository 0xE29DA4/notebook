# npm

```shell
# 查看项目包安装目录
npm root
# 查看全局包安装目录
npm root -g

# 安装所有依赖
npm install
# 安装指定依赖
npm install PACKAGE
# 使用镜像
npm install PACKAGE --registry=https://registry.npm.taobao.org
# 安装仅开发期间使用的依赖
npm install -D PACKAGE

# 卸载依赖
npm uninstall PACKAGE
npm remove PACKAGE

# 更新项目依赖
npm update <package_name>
# 更新全局包
npm update -g <package_name>

# 运行脚本
npm run SCRIPT

# 设置镜像，以淘宝镜像为例
npm config set registry https://registry.npm.taobao.org
# 打开 npm 配置文件
npm config edit

# 登录 npm
npm login
```

#### yarn

```sh
# 安装 Yarn
npm i -g yarn

# 安装所有依赖
yarn
# 安装制定依赖
yarn add PACKAGE
# 安装仅开发期间使用的依赖
yarn add -D PACKAGE

# 卸载依赖
yarn remove PACKAGE

# 运行脚本
yarn SCRIPT

# 获取二进制文件地址以添加环境变量
yarn global bin
```

#### pnpm

```shell
# 安装 PNPM
npm install -g pnpm

# 安装所有依赖
pnpm install
# 安装依赖
pnpm add PACKAGE
# 安装仅开发期间使用的依赖
pnpm add -D PACKAGE

# 卸载依赖
pnpm remove PACKAGE

# 运行脚本
pnpm SCRIPT
```
