#### 基本命令

```shell
# 安装特定版本的 X
pip install X==6.1.0

# 查看已安装的包，包括基本包
pip list
# 查看已安装的包，不包括基本包
pip freeze
```

#### venv

> Python 3.3+ 内置，仅支持 Python 3.3+，只能创建当前 Python 版本的环境

```shell
# 创建一个虚拟环境
python -m venv <env_name>

# 激活虚拟环境
source <env_name>/bin/activavte
# Windows 环境
<env_name>/Scripts/activavte

# 停用虚拟环境
deactivate

# 删除虚拟环境
rm -rf <env_name>
```

#### virtualenv

> 支持 Python 2.7 与 Python 3.x，可指定 Python 版本

```shell
# 安装基本依赖
# windows 系统需要额外安装 virtualenvwrapper-win
pip install virtualenv

# 创建新的虚拟环境
mkvirtualenv <虚拟环境名>

# 查看已有虚拟环境
workon

# 进入虚拟环境
workon <虚拟环境>

# 删除虚拟环境
rmvirtualenv <虚拟环境名>
```
