# UV - Python 包管理器

UV 是高性能的 Python 包管理器，设计用于替代 pip 和 pip-tools。

## 安装 UV

```bash
curl -LsSf 'https://astral.sh/uv/install.sh' | sh
```

## 常用命令

### 安装包

```bash
uv pip install pandas
```

### 从 requirements.txt 安装

```bash
uv pip install -r requirements.txt
```

### 生成 requirements.txt

```bash
uv pip freeze > requirements.txt
```

### 卸载包

```bash
uv pip uninstall pandas
```

### 创建虚拟环境

```bash
uv venv .venv
```

## 性能优势

- 比 pip 快 10-100 倍
- 支持并发下载和缓存优化
