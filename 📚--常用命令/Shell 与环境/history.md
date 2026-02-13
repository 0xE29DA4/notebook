# history

> 显示或操作历史命令列表。

- 查看历史命令相关变量
  ```shell
  echo $HISTSIZE  # 查看历史命令记录最大数目
  echo $HISTFILE  # 查看历史命令记录文件路径
  ```

- 管理历史记录
  ```shell
  history -r <file>  # 从文件恢复历史记录
  history -c         # 清空当前历史记录
  ```

- 历史命令调用
  ```shell
  !3006  # 执行第 3006 条历史命令
  !!     # 执行上一条命令
  ```
