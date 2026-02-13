# tar

> Tape Archive，打包和解包工具 (Linux 下最常用)。

- 打包并压缩为 .tar.gz (c: create, z: gzip, v: verbose, f: file)
  ```shell
  tar czvf archive.tar.gz /path/to/directory
  ```

- 解压 .tar.gz 文件 (x: extract)
  ```shell
  tar xzvf archive.tar.gz
  ```

- 列出归档内容 (t: list)
  ```shell
  tar tf archive.tar.gz
  ```
