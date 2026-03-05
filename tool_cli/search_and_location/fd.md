# fd

> find 的现代化替代品，更快速、更友好的文件搜索工具。
> 更多信息：<https://github.com/sharkdp/fd>

- 递归搜索当前目录中匹配模式的文件：
  `fd "{{模式}}"`

- 搜索指定目录：
  `fd "{{模式}}" {{路径}}`

- 搜索文件名并执行命令：
  `fd "{{模式}}" --exec {{命令}}`

- 按扩展名搜索：
  `fd --extension {{txt}}`

- 搜索隐藏文件和被忽略的文件：
  `fd --hidden --no-ignore "{{模式}}"`

- 只搜索目录：
  `fd --type directory "{{模式}}"`

- 搜索并排除某些目录：
  `fd --exclude {{node_modules}} "{{模式}}"`

- 使用正则表达式搜索：
  `fd "{{.*\.(js|ts)$}}"`
