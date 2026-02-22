# Git

## git 配置

```shell
# 配置全局邮箱
git config --global user.email "<你的邮箱>"
# 配置全局姓名
git config --global user.name "<你的名字>"
# 重置某项配置
git config --global --unset http.proxy
# 设置仓库初始化时默认的分支名
git config --global init.defaultBranch main
# 查看配置信息
git config --list
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
# 修改关联远程仓库
git remote set-url origin REMOTE_REPO_URL
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
