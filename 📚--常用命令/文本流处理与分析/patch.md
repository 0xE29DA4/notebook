# patch

> 用于将补丁文件应用到原始文件，从而将其更新为修改后的文件，常与 diff 一起使用。

- 应用补丁
  ```shell
  patch FILE OPTION < file.patch
  ```

- 撤销补丁
  ```shell
  patch -R < file.patch
  ```
