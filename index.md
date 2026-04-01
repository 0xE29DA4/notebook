# 欢迎

Hello, world!

## 💻 开发笔记

软件开发相关的配置、实践与学习笔记

### 后端开发

- [PostgreSQL](dev_backend/postgres) - PostgreSQL 数据库配置与使用
- [Redis](dev_backend/redis/index.md) - Redis 内存数据库配置与使用

### 前端开发

- [Bun](tool_dev/bun/index.md) - Bun JavaScript 运行时与工具链

### 硬件开发

- [QEMU](dev_hardware/qemu/index.md) - QEMU 硬件虚拟化与模拟器
- [RISC-V](dev_hardware/risc-v/index.md) - RISC-V 开源指令集架构
- [STM32](dev_hardware/stm32/index.md) - STM32 嵌入式开发

---

## 🎓 计算机科学

CS 核心课程笔记与知识整理

- [编译原理](learn_cs/compiler_principles) - 词法分析、语法分析、代码生成
- [计算机网络](learn_cs/computer_network) - TCP/IP、HTTP、DNS
- [计算机组成原理](learn_cs/computer_organization) - CPU、存储、总线
- [数据结构与算法](learn_cs/data_structures_and_algorithms) - 线性表、树、图、排序、搜索
- [操作系统](learn_cs/operating_system) - 进程、内存、文件系统

---

## 📐 数学

数学基础与进阶笔记

- [抽象代数](learn_math/abstract_algebra) - 群、环、域理论
- [微积分](learn_math/calculus) - 极限、导数、积分
- [初等代数](learn_math/elementary_algebra) - 代数基础
- [初等数论](learn_math/elementary_number_theory) - 整数、素数、同余
- [图论](learn_math/graph_theory) - 图、路径、网络流
- [线性代数](learn_math/linear_algebra) - 向量、矩阵、线性变换
- [概率论](learn_math/probability_theory) - 概率、随机变量、分布

---

## 📝 领域特定语言

- [CSS](learn_dsl/css.md) - 层叠样式表
- [LaTeX](learn_dsl/latex.md) - 排版系统
- [Markdown](learn_dsl/markdown.md) - 轻量级标记语言

---

## 🛠️ 命令行工具

现代化的命令行工具速查手册，采用 tldr-page 风格编写

### 基础文件操作

- [cd](tool_cli/basic_file_operations/cd.md) - 切换工作目录
- [cp](tool_cli/basic_file_operations/cp.md) - 复制文件或目录
- [dd](tool_cli/basic_file_operations/dd.md) - 低级复制与转换
- [file](tool_cli/basic_file_operations/file.md) - 识别文件类型
- [ln](tool_cli/basic_file_operations/ln.md) - 创建链接
- [ls](tool_cli/basic_file_operations/ls.md) - 列出目录内容
- [mkdir](tool_cli/basic_file_operations/mkdir.md) - 创建目录
- [mv](tool_cli/basic_file_operations/mv.md) - 移动或重命名文件
- [pwd](tool_cli/basic_file_operations/pwd.md) - 显示当前目录
- [readlink](tool_cli/basic_file_operations/readlink.md) - 读取链接内容
- [rm](tool_cli/basic_file_operations/rm.md) - 删除文件或目录
- [rmdir](tool_cli/basic_file_operations/rmdir.md) - 删除空目录
- [stat](tool_cli/basic_file_operations/stat.md) - 显示文件状态
- [touch](tool_cli/basic_file_operations/touch.md) - 更新文件时间戳
- [tree](tool_cli/basic_file_operations/tree.md) - 以树状结构列出目录

### 搜索与定位

- [fd](tool_cli/search_and_location/fd.md) - 快速文件搜索
- [rg](tool_cli/search_and_location/rg.md) - ripgrep 模式搜索
- [whereis](tool_cli/search_and_location/whereis.md) - 定位二进制文件
- [which](tool_cli/search_and_location/which.md) - 定位可执行文件

### 文本预览与提取

- [bat](tool_cli/text_preview_and_extraction/bat.md) - 增强的 cat 命令
- [cat](tool_cli/text_preview_and_extraction/cat.md) - 连接并显示文件内容

### 文本流处理与分析

- （待补充）

### 归档与压缩

- [bzip2](tool_cli/archive_and_compression/bzip2.md) - bzip2 压缩工具
- [gzip](tool_cli/archive_and_compression/gzip.md) - gzip 压缩工具
- [tar](tool_cli/archive_and_compression/tar.md) - 归档工具
- [unzip](tool_cli/archive_and_compression/unzip.md) - 解压 zip 文件
- [xz](tool_cli/archive_and_compression/xz.md) - xz 压缩工具
- [zip](tool_cli/archive_and_compression/zip.md) - zip 压缩工具

### 进程与任务管理

- [jobs](tool_cli/process_and_task_management/jobs.md) - 显示作业状态
- [journalctl](tool_cli/process_and_task_management/journalctl.md) - 查询 systemd 日志
- [kill](tool_cli/process_and_task_management/kill.md) - 终止进程
- [pkill](tool_cli/process_and_task_management/pkill.md) - 按名称终止进程
- [procs](tool_cli/process_and_task_management/procs.md) - 增强的 ps 命令
- [systemctl](tool_cli/process_and_task_management/systemctl.md) - systemd 服务控制

### 网络与通信

- [curl](tool_cli/network_and_communication/curl.md) - 命令行 HTTP 客户端
- [doggo](tool_cli/network_and_communication/doggo.md) - 现代 DNS 查询工具
- [frp](tool_cli/network_and_communication/frp.md) - 快速反向代理
- [firewalld](tool_cli/network_and_communication/firewalld.md) - 防火墙管理
- [host](tool_cli/network_and_communication/host.md) - DNS 查询
- [ip](tool_cli/network_and_communication/ip.md) - 网络配置
- [ipcs](tool_cli/network_and_communication/ipcs.md) - IPC 状态
- [mtr](tool_cli/network_and_communication/mtr.md) - 网络诊断工具
- [ncat](tool_cli/network_and_communication/ncat.md) - 网络工具（nc 的替代）
- [networkctl](tool_cli/network_and_communication/networkctl.md) - 网络链路状态
- [nmap](tool_cli/network_and_communication/nmap.md) - 网络扫描器
- [ping](tool_cli/network_and_communication/ping.md) - ICMP 回显测试
- [resolvectl](tool_cli/network_and_communication/resolvectl.md) - DNS 解析器控制
- [rsync](tool_cli/network_and_communication/rsync.md) - 远程同步
- [scp](tool_cli/network_and_communication/scp.md) - 安全复制
- [ss](tool_cli/network_and_communication/ss.md) - 套接字统计
- [ssh](tool_cli/network_and_communication/ssh.md) - 安全 Shell 客户端
- [ssh-copy-id](tool_cli/network_and_communication/ssh-copy-id.md) - 复制 SSH 公钥
- [ssh-keyscan](tool_cli/network_and_communication/ssh-keyscan.md) - 收集 SSH 公钥
- [tcpdump](tool_cli/network_and_communication/tcpdump.md) - 网络包分析器
- [tracepath](tool_cli/network_and_communication/tracepath.md) - 追踪到主机的路径
- [wg](tool_cli/network_and_communication/wg.md) - WireGuard VPN 工具
- [wget](tool_cli/network_and_communication/wget.md) - 命令行下载器

### 磁盘与文件系统

- [chroot](tool_cli/disk_and_filesystem/chroot.md) - 改变根目录
- [duf](tool_cli/disk_and_filesystem/duf.md) - 增强的 df 命令
- [dust](tool_cli/disk_and_filesystem/dust.md) - 增强的 du 命令
- [fdisk](tool_cli/disk_and_filesystem/fdisk.md) - 磁盘分区管理
- [lsblk](tool_cli/disk_and_filesystem/lsblk.md) - 列出块设备
- [mkfs](tool_cli/disk_and_filesystem/mkfs.md) - 创建文件系统
- [mount](tool_cli/disk_and_filesystem/mount.md) - 挂载文件系统
- [umount](tool_cli/disk_and_filesystem/umount.md) - 卸载文件系统

### Shell 与环境

- [alias](tool_cli/shell_and_environment/alias.md) - 命令别名
- [basename](tool_cli/shell_and_environment/basename.md) - 获取文件名
- [dirname](tool_cli/shell_and_environment/dirname.md) - 获取目录名
- [echo](tool_cli/shell_and_environment/echo.md) - 输出文本
- [env](tool_cli/shell_and_environment/env.md) - 显示环境变量
- [export](tool_cli/shell_and_environment/export.md) - 导出变量
- [expr](tool_cli/shell_and_environment/expr.md) - 表达式求值
- [false](tool_cli/shell_and_environment/false.md) - 返回失败状态
- [history](tool_cli/shell_and_environment/history.md) - 命令历史
- [printenv](tool_cli/shell_and_environment/printenv.md) - 打印环境变量
- [read](tool_cli/shell_and_environment/read.md) - 读取输入
- [seq](tool_cli/shell_and_environment/seq.md) - 生成序列
- [set](tool_cli/shell_and_environment/set.md) - 设置 shell 选项
- [shift](tool_cli/shell_and_environment/shift.md) - 移位位置参数
- [sleep](tool_cli/shell_and_environment/sleep.md) - 延迟执行
- [source](tool_cli/shell_and_environment/source.md) - 执行脚本
- [tee](tool_cli/shell_and_environment/tee.md) - 读取并写入
- [test](tool_cli/shell_and_environment/test.md) - 条件测试
- [true](tool_cli/shell_and_environment/true.md) - 返回成功状态
- [type](tool_cli/shell_and_environment/type.md) - 显示命令类型
- [unset](tool_cli/shell_and_environment/unset.md) - 取消变量
- [xargs](tool_cli/shell_and_environment/xargs.md) - 构建并执行命令

### 系统信息与状态

- [date](tool_cli/system_info_and_status/date.md) - 显示或设置日期时间
- [dmesg](tool_cli/system_info_and_status/dmesg.md) - 内核环形缓冲区
- [free](tool_cli/system_info_and_status/free.md) - 内存使用情况
- [hostnamectl](tool_cli/system_info_and_status/hostnamectl.md) - 主机名控制
- [localectl](tool_cli/system_info_and_status/localectl.md) - 本地化控制
- [lsof](tool_cli/system_info_and_status/lsof.md) - 列出打开的文件
- [systemd-analyze](tool_cli/system_info_and_status/systemd-analyze.md) - systemd 性能分析
- [systemd-cgls](tool_cli/system_info_and_status/systemd-cgls.md) - cgroup 树状视图
- [systemd-cgtop](tool_cli/system_info_and_status/systemd-cgtop.md) - cgroup 资源监控
- [timedatectl](tool_cli/system_info_and_status/timedatectl.md) - 时间控制
- [uname](tool_cli/system_info_and_status/uname.md) - 系统信息
- [uptime](tool_cli/system_info_and_status/uptime.md) - 系统运行时间
- [watch](tool_cli/system_info_and_status/watch.md) - 周期性执行命令

### NixOS 系统管理

- [home-manager](tool_cli/nixos_system_management/home-manager.md) - Home Manager 配置
- [nh](tool_cli/nixos_system_management/nh.md) - NixOS 帮助工具
- [nix-collect-garbage](tool_cli/nixos_system_management/nix-collect-garbage.md) - 清理 Nix 存储
- [nix-env](tool_cli/nixos_system_management/nix-env.md) - Nix 包管理
- [nix-flake](tool_cli/nixos_system_management/nix-flake.md) - Nix Flakes 管理
- [nix-run](tool_cli/nixos_system_management/nix-run.md) - 运行 Nix 包
- [nix-search](tool_cli/nixos_system_management/nix-search.md) - 搜索 Nix 包
- [nix-shell](tool_cli/nixos_system_management/nix-shell.md) - Nix Shell 环境
- [nix-store](tool_cli/nixos_system_management/nix-store.md) - Nix 存储
- [nixos-option](tool_cli/nixos_system_management/nixos-option.md) - 查询 NixOS 配置
- [nixos-rebuild](tool_cli/nixos_system_management/nixos-rebuild.md) - 重建 NixOS 系统

### 开发工具与调试

- [gdb](tool_cli/dev_tools_and_debugging/gdb.md) - GNU 调试器
- [ldd](tool_cli/dev_tools_and_debugging/ldd.md) - 列出动态库依赖
- [nm](tool_cli/dev_tools_and_debugging/nm.md) - 列出符号表
- [openssl](tool_dev/openssl/index.md) - OpenSSL 工具集
- [readelf](tool_cli/dev_tools_and_debugging/readelf.md) - 显示 ELF 信息
- [strace](tool_cli/dev_tools_and_debugging/strace.md) - 系统调用追踪

### 用户与权限

- （待补充）

---

## 🔧 工具链与开发工具

### 编译调试工具链

- [CMake](tool_toolchain/cmake.md) - 跨平台构建系统
- [Clang](tool_toolchain/clang.md) - LLVM 编译器前端
- [GCC](tool_toolchain/gcc.md) - GNU 编译器集合
- [Makefile](tool_toolchain/make.md) - GNU Make 构建脚本

### 开发工具

- [Git](tool_dev/git/index.md) - 版本控制系统
- [Podman](tool_dev/podman/index.md) - 容器运行时
- [PyTorch](tool_dev/pytorch/index.md) - 深度学习框架

### 多媒体工具

- [FFmpeg](tool_media/ffmpeg/index.md) - 音视频处理工具

---

## 关于

本站使用 [Quartz](https://quartz.jzhao.xyz/) 构建，托管于 GitHub Pages。

个人使用，不接受批评。

---
