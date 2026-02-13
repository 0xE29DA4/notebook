# diff

> 用于查看文件差异，以及生成补丁文件，常与 patch 一起使用。

- 对比差异
  ```shell
  diff [option] file1 file2
  # -u/--unified: 以统一的格式输出差异，这种格式更易读，也是生成补丁文件的常用格式
  # -r: 递归比较目录下的所有文件
  # -N: 将不存在的文件视为空文件
  # -p: 显示差异所在的函数
  # -i: ignore case
  # -w: 忽略空格
  ```

- 生成补丁文件
  ```shell
  diff [option] file1 file2 > file.patch
  ```
