# Git

## git 配置

```shell
git config --global user.email "<你的邮箱>"   # 配置全局邮箱
git config --global user.name "<你的名字>"    # 配置全局姓名
git config --global --unset http.proxy        # 重置某项配置
# 设置仓库初始化时默认的分支名
git config --global init.defaultBranch main
git config --list                             # 查看配置信息
```

## git 项目初始化

```shell
cd PROJECT_ROOT
# 初始化本地仓库
git init
```

## 暂存区操作

```shell
# add
git add FILE                       # 将文件的修改添加到暂存区
git add DIR                        # 将目录的修改添加到暂存区
git add .                          # 将当前目录所有文件、目录的修改添加到暂存区

# reset
git reset FILE                     # 将暂存区某个文件取消暂存
git reset --hard VER               # 回退到某个版本
```

## 版本库操作

```shell
git commit -m COMMENT             # 提交暂存区指定文件到版本库
```

## 仓库状态

```shell
git status                        # 查看本地仓库状态
git status -s                     # 简要版
```

## 日志

```shell
git log                           # 查看日志
```

## remote

```shell
git remote                                                        # 查看远程仓库
git remote -v                                                     # 查看远程仓库的详细信息
git remote add origin REMOTE_REPO_URL                             # 关联远程仓库
```

## 推送到远端

```shell
git push -u orgin LOCAL_BRANCH                      # 设置上游并推送到远程仓库
git push REMOTE_HOST LOCAL_BRANCH:REMOTE_BRANCH     # 推送到远程仓库
git push REMOTE_HOST LOCAL_BRANCH                   # 如果本地分支与远端分支名相同
git push --force REMOTE_HOST LOCAL_BRANCH           # 强制 push
git push REMOTE_HOST TAG_NAME                       # 将标签推送到远程仓库
```

## pull

```shell
git pull REMOTE_BRANCH LOCAL_BRANCH         # 从远程仓库获取最新版本合并到本地分支
```

## branch

```shell
git branch                                  # 查看所有本地分支
git branch -r                               # 查看所有远程分支
git branch -a                               # 查看所有分支
git branch BRANCH_NAME                      # 新建一个本地分支
git branch -d BRANCH_NAME                   # 删除本地分支
git branch -D BRANCH_NAME                   # 强制删除本地分支
git branch -d -r BRANCH_NAME                # 删除远程分支
git branch -m OLD NEW                       # 重命名本地分支
git branch -M OLD NEW                       # 强制重命名本地分支
git branch --set-upstream-to=origin/REMOTE_BRANCH LOCAL_BRANCH    # 为本地分支设置上游远程分支
git branch --unset-upstream BRANCH_NAME     # 取消本地分支对上游分支的追踪
```

## checkout

```shell
git checkout BRANCH_NAME                      # 切换到分支
git checkout -b BRANCH_NAME                   # 创建并切换到分支
```

## merge

```shell
git merge BRANCH_NAME                # 将指定分支合并到当前分支
```

## tag

```shell
git tag                           # 列出已有的标签
git tag TAG_NAME                  # 创建一个标签
git tag -d TAG_NAME               # 删除一个标签
```

## 使用 github actions 建立 CI/CD 工作流

1. 在你的项目根目录下，创建一个名为 `.github/workflows` 的文件夹
2. 在该文件夹下，创建一个 YAML 文件，比如叫 `rust-ci.yml`
3. 编写 yaml 文件

下面是一个 yaml 文件的例子

```yaml
# 工作流的名称，会显示在 GitHub Actions 页面
name: Rust CI/CD

# 触发工作流的事件
on:
  # 当有代码 push 到 main 分支时触发
  push:
    branches: [ "main" ]
  # 也可以手动触发
  workflow_dispatch:

# 定义环境变量，方便复用
env:
  # 我们要构建的 Docker 镜像的名称
  IMAGE_NAME: ${{ github.repository_owner }}/${{ github.event.repository.name }}

# 工作流包含的任务 (jobs)
jobs:
  # 第一个任务：构建和测试
  build_and_test:
    # 任务的名称
    name: Build & Test
    # 运行此任务的虚拟机环境
    runs-on: ubuntu-latest

    # 任务的步骤 (steps)
    steps:
      # 第一步：获取代码
      - name: Check out repository code
        uses: actions/checkout@v4

      # 第二步：安装和缓存 Rust 工具链
      - name: Install Rust toolchain
        uses: dtolnay/rust-toolchain@stable

      # 第三步：运行测试
      - name: Run tests
        run: cargo test --verbose

  # 第二个任务：构建并推送 Docker 镜像
  build_and_push_docker:
    # 任务的名称
    name: Build & Push Docker Image
    # 运行此任务的虚拟机环境
    runs-on: ubuntu-latest
    # 设置依赖：这个任务必须等待 build_and_test 任务成功完成后才能开始
    needs: build_and_test

    # 授予此任务向 GHCR 推送镜像的权限
    permissions:
      contents: read
      packages: write

    # 任务的步骤
    steps:
      # 第一步：获取代码
      - name: Check out repository code
        uses: actions/checkout@v4

      # 第二步：登录到 GitHub Container Registry (GHCR)
      - name: Log in to the Container registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          # ${{ github.actor }} 是你的 GitHub 用户名
          # ${{ secrets.GITHUB_TOKEN }} 是 GitHub 自动为你生成的临时密码，非常安全
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      # 第三步：从镜像名中提取元数据（比如标签）
      - name: Extract metadata for Docker
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ env.IMAGE_NAME }}

      # 第四步：构建并推送 Docker 镜像
      # 这一步会使用你项目中的 Dockerfile
      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

将这些改动推送到远程仓库，打开你的 GitHub 仓库页面，点击顶部的 "Actions" 标签，
你马上就能看到一个正在运行的工作流，你可以点进去，实时查看每一步的日志输出。如果一切顺利，它会显示绿色的对勾。完成后，你可以在你的 GitHub 主页的 "Packages" 部分找到刚刚被推送上来的 Docker 镜像
