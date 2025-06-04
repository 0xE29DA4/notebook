# git

## config

```shell
git config --global user.email "<你的邮箱>" # 配置 global 邮箱
git config --global user.name "<你的名字>" # 配置 global 姓名
git config --global --unset http.proxy # 重置代理
git config --list # 查看配置信息
```

## init

```shell
# 初始化本地仓库
cd <项目目录>
git init
```

## add

```shell
git add <file> # 将文件的修改添加到暂存区
git add <dir> # 将目录的修改添加到暂存区
git add . # 将当前目录所有文件、目录的修改添加到暂存区
```

## reset

```shell
git reset <file> # 将暂存区的文件取消暂存
git reset --hard <版本号> # 回退到某个版本
```

## commit

```shell
git commit <file> -m "comment" # 提交暂存区指定文件到版本库
git commit -m "comment" # 提交暂存区所有改变到版本库
```

## status

```shell
git status # 查看自上次提交后的改动
git status -s # 简要版
```

## log

```shell
git log # 查看日志
```

## remote

```shell
git remote # 查看远程仓库
git remote -v # 查看远程仓库的详细信息
git remote add <远端仓库名> <远端仓库URL> # 关联远程仓库
```

## push

```shell
git push <远端主机> <本地分支>:<远端分支> # 推送到远程仓库
git push <远端主机> <本地分支> # 如果本地分支与远端分支名相同
git push --force <远端主机> <本地分支> # 强制 push
git push -u orgin [本地分支] # 设置上游并推送到远程仓库
git push [远端主机] [tag_name] # 将标签推送到远程仓库
```

## pull

```shell
git pull [远端分支] [本地分支] # 从远程仓库获取最新版本合并到本地分支
```

## branch

```shell
git branch    # 查看所有本地分支
git branch -r # 查看所有远程分支
git branch -a # 查看所有分支
git branch [新本地分支] # 新建一个本地分支
git branch -d <本地分支> # 删除本地分支
git branch -d -r <远程分支> # 删除远程分支
git branch -D <本地分支> # 强制删除本地分支
git branch -m <old> <new> # 重命名本地分支
git branch --unset-upstream [本地分支名] # 取消本地分支对上游分支的追踪
```

## checkout

```shell
git checkout [分支名] # 切换到分支
git checkout -b [新分支] # 创建并切换到分支
git checkout -b [新分支名] [标签名] # 基于某个标签创建一个新分支
```

## merge

```shell
git merge [分支名] # 将指定分支合并到当前分支
```

## tag

```shell
git tag # 列出已有的标签
git tag [tag_name] # 创建一个标签
```
