# uniq

> 报告或省略重复的行 (注意：uniq 只能检测相邻的重复行，通常配合 sort 使用)。

- 去除相邻重复行
  ```shell
  sort file.txt | uniq
  ```

- 统计每行出现的次数
  ```shell
  sort file.txt | uniq -c
  ```

- 只显示重复的行
  ```shell
  sort file.txt | uniq -d
  ```
