# readelf

> 用于显示 ELF (Executable and Linkable Format) 文件的信息。

- 查看文件头信息
  ```shell
  readelf -h file
  ```

- 查看所有信息
  ```shell
  readelf -a file
  ```

- 查看段头表 (Program Headers)
  ```shell
  readelf -l file
  ```

- 查看节头表 (Section Headers)
  ```shell
  readelf -S file
  ```

- 查看符号表 (Symbols)
  ```shell
  readelf -s file
  ```
