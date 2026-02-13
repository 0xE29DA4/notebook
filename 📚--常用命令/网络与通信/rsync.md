# rsync

> 快速、多功能甚至远程的文件复制工具。

- 常用同步命令
  ```shell
  rsync [option] src dst

  # 常用选项:
  # -a: archive，归档模式，通常是必用的 (等于 -rlptgoD)
  # -v: verbose，显示详细信息
  # -z: 压缩传输
  # -r: 递归同步
  # -u: update，仅更新较新的文件
  # --progress: 显示进度
  ```

- 通过 SSH 同步并删除目标端多余文件
  ```shell
  rsync -avz --delete -e ssh src/ user@host:dst/
  ```

- 排除指定文件
  ```shell
  rsync -av --exclude "*.tmp" src/ dst/
  ```
