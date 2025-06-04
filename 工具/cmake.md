# CMake

## 命令

|命令                |备注                        |
| -                 | -                          |
| -S 目录            | 指定 CMake 工程位置         |
| -B 目录            | 指定 CMake 构建输出路径      |
| -G 生成器          | generate，生成项目          |
| --build 目录       | 构建项目                   |
| start 项目         | 启动一个已生成的项目         |

## 预定义变量

| 变量                      | 备注                          |
| ----                     | ----                          |
| PROJECT_SOURCE_DIR       | 根级 CMakeLists 所在的路径      |
| CMAKE_CURRENT_SOURCE_DIR | 当前 CMakeLists 所在的路径      |
| CMAKE_BUILD_TYPE         | 设定编译类型（Debug 或 Release） |
| CMAKE_CXX_FLAG           | C++语言编译器编译选项            |

## 基本配置

```cmake
# 最低 CMake 版本
cmake_minimum_required(VERSION 3.26)

# 声明项目属性
project(
    project_name
    LANGUAGES CXX C
    VERSION 0.0.1
    DESCRIPTION "对此项目的描述"
)

# 设置语言标准
set(CMAKE_CXX_STANDARD 17)

# 设置编译器
set(CMAKE_C_COMPILER "/usr/lib/clang")
set(CMAKE_CXX_COMPILER "/usr/bin/clang++")

# 如果项目基于 makefile 或者 ninja，需要开启如下功能，才能开启语言服务器
set(EXPORT_COMPILE_COMMANDS ON)

# 指定头文件目录 
include_directories(${PROJECT_SOURCE_DIR}/includeA ${PROJECT_SOURCE_DIR}/includeB)
# 也可以为目标指定头文件目录
# target_include_directories(project_name PRIVATE "./includeA")

# 将 src 中的源文件添加到变量 SRC_LIST 中
aux_source_directory(${PROJECT_SOURCE_DIR}/src SRC_LIST)
# 也可以使用 glob 搜索文件添加到变量 SRC_LIST
# file(GLOB SRC_LIST ${PROJECT_SOURCE_DIR}/src/*.cpp)

# 指定可执行文件的生成目录
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

# 输出可执行文件
add_executable(
    a.out
    ${SRC_LIST}
)
```

## 字符串

```cmake
# 字符串拼接
# new_str 是 str1 和 str2 拼接的结果
set(new_str str1 str2)

# 字符串追加，将 str1 和 str2 追加到 str 中
list(APPEND ${str} str1 str2)

# 字符串移除，将 str1 和 str2 从 str 中移除
list(REMOVE_ITEM ${str} str1 str2)
```

## 库

```cmake
# 指定库输出路径
set(LIBRARY_OUTPUT_PATH 输出路径)

# 因为 linux 下动态库具有可执行权限，而静态库没有
# 下面的可以生成动态库，但不能生成静态库
set(EXECUTABLE_OUTPUT_PATH 输出路径)

# 生成库
# 动态：SHARED，静态：STATIC
add_library(lib_name STATLC src)

# 链接库到所有目标
# 1. 指定库的路径
link_directories(库所在路径)
# 2. 链接静态库
link_libraries(lib_name)

# 链接库到指定目标
target_link_directories(target PUBLIC 库所在路径)
target_link_libraries(target 要连接的库)

# 输出库
add_executable(lib_name <files.cpp>)
# or
add_libraries(lib_name [SHARED] ${src})
```

## 消息

```cmake
# 不加 STAUTS 默认被当作一条重要消息
message(STATUS "src: ${src}")
```

## 其他

```cmake
# 设置父节点，父节点的变量对子节点可见，子目录下需要有一个CMakeLists
add_subdirectory(<子目录>)

# 添加宏 DEBUG
add_definitions(-DDEBUG)

# 添加编译选项
add_compile_options(-g -Wunused)

# 为一个指定目标添加编译选项
target_compile_options(a.out PUBLIC -Wall -Werror)

# todo:
target_compile_features(app PRIVATE cxx_std_11)

# 编译开关，默认为off
option(OPTION0 "description" OFF)
if (OPTION0)
    # ...
endif()

# 判断工程是不是顶层工程
if (PROJECT_IS_TOP_LEVEL)

# 循环
foreach(var in list)
    message("${var}")
endforeach()
```
