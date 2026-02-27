# Git

## git config

```sh
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

## git init

```sh
cd PROJECT_ROOT
# 初始化本地仓库
git init
```

## git add

```sh
# add
# 将文件的修改添加到暂存区
git add FILE
# 将目录的修改添加到暂存区
git add DIR
# 将当前目录所有文件、目录的修改添加到暂存区
git add .
```

## git rm

```sh
# 同时删除工作区和暂存区的文件
git rm FILE
# 递归删除
git rm -f DIR
# 从暂存区移除文件并停止跟踪
git rm --cached FILE
```

## git clean

```sh
# 删除所有未跟踪的文件
git clean -f
# 删除所有未跟踪的目录
git clean -d
# 删除未跟踪文件和目录
git clean -fd
# 预览将要删除的文件
git clean --dry-run
```

## git reset

reset 可能会造成悬空的 commit，但这些 commit 其实并没有被立即删除，Git 还会保留它们一段时间，你可以通过 git reflog 找回来

```sh
# 回退分支到上一个 commit，不重置暂存区和工作目录
git reset --soft HEAD~1
# 回退分支到上一个 commit，不重置工作目录
git reset --mixed HEAD~1
# 彻底回退到某个版本
git reset --hard COMMIT
```

## git restore

```sh
# 放弃工作区的修改
git restore FILE
# 撤销对文件的暂存
git restore --staged FILE
# 从某个 commit 恢复单个文件内容
git restore --source=HEAD~2 <file>
```

## git commit

```sh
# 提交暂存区所有文件到版本库
git commit -m COMMENT
```

## git status

```sh
# 查看本地仓库状态
git status
# 简要版
git status -s
```

## git diff

```sh
# 查看差异
# 查看工作区与暂存区之间的差异
git diff
# 查看暂存区与最新提交之间的差异
git diff --staged
# 查看两个提交之间的差异
git diff COMMIT1 COMMIT2
# 查看特定文件在两个提交之间的差异
git diff COMMIT1 COMMIT2 -- FILE
# 查看工作目录和特定提交之间的差异
git diff COMMIT

# 输出格式
# 只显示文件名
git diff --name-only COMMIT1 COMMIT2
# 补丁格式差异
git diff --patch COMMIT1 COMMIT2
```

## git log

```sh
# 查看日志
git log
# 查看日志，以及改动
git log --stat
# 查看日志，以图形方式
git log --graph
# 查看日志，以一条线的方式
git log --online
```

## git remote

```sh
# 查看远程仓库
git remote
# 查看远程仓库的详细信息
git remote -v
# 查看特定远程仓库
git remote show origin
# 关联远程仓库
git remote add origin REMOTE_REPO_URL
# 修改关联远程仓库
git remote set-url origin REMOTE_REPO_URL
```

## git push

```sh
# 设置上游并推送到远程仓库
git push -u orgin LOCAL_BRANCH
# 推送到远程仓库
git push REMOTE_HOST LOCAL_BRANCH:REMOTE_BRANCH
# 如果本地分支与远端分支名相同
git push REMOTE_HOST LOCAL_BRANCH
# 强制 push
git push --force REMOTE_HOST LOCAL_BRANCH
# 将标签推送到远程仓库
git push REMOTE_HOST TAG_NAME
```

## git pull

```sh
# 从远程仓库获取最新版本合并到本地分支
git pull REMOTE_BRANCH LOCAL_BRANCH
```

## git branch

```sh
# 查看所有本地分支
git branch
# 查看所有本地分支以及当前提交 SHA 与 commit message
git branch -v
# 查看所有本地分支以及当前提交 SHA 与 commit message 与上游分支
git branch -v
# 查看所有远程分支
git branch -r
# 查看所有分支
git branch -a
# 新建一个本地分支
git branch BRANCH_NAME
# 删除本地分支
git branch -d BRANCH_NAME
# 强制删除本地分支
git branch -D BRANCH_NAME
# 删除远程分支
git branch -d -r BRANCH_NAME
# 重命名本地分支
git branch -m OLD NEW
# 强制重命名本地分支
git branch -M OLD NEW
# 为本地分支设置上游远程分支
git branch --set-upstream-to=REMOTE_NAME/REMOTE_BRANCH LOCAL_BRANCH
# 取消本地分支对上游分支的追踪
git branch --unset-upstream BRANCH_NAME
```

## git checkout

```sh
# 检出到分支
git checkout BRANCH_NAME
# 检出到标签
git checkout TAG_NAME
# 创建并切换到分支
git checkout -b BRANCH_NAME
# 创建基于标签的分支
git checkout -b BRANCH_NAME TAG_NAME
```

## git merge

```sh
# 将指定分支合并到当前分支
git merge BRANCH_NAME
```

## git tag

```sh
# 列出已有的标签
git tag
# 创建一个标签
git tag TAG_NAME
# 创建带注释的标签
git tag -a TAG_NAME -m "标签说明信息"
# 创建带签名的标签
git tag -s TAG_NAME -m "标签说明信息"
# 查看标签详情
git show TAG_NAME
# 删除一个标签
git tag -d TAG_NAME
```
