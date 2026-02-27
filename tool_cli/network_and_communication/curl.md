# curl

> 传输数据的命令行工具。
> 更多信息：<https://manned.org/curl>

- 发送 GET 请求并输出到文件：
  `curl -o {{文件名}} {{URL}}`

- 发送 GET 请求并使用远程文件名保存：
  `curl -O {{URL}}`

- 查看响应头和响应体：
  `curl -i {{URL}}`

- 查看详细的通信过程：
  `curl -v {{URL}}`

- 跟随 HTTP 重定向：
  `curl -L {{URL}}`

- 发送 POST 请求带表单数据：
  `curl -X POST -d "{{key1=value1&key2=value2}}" {{URL}}`

- 发送 POST 请求带 JSON 数据：
  `curl -X POST -H "Content-Type: application/json" -d '{{{"key": "value"}}}' {{URL}}`

- 发送文件上传请求：
  `curl -F "file=@{{文件路径}}" {{URL}}`

- 发送表单：
  `curl -F "data: 666" {{URL}}`

- 发送文件，从 stdin 获取文件输入
  `curl -F "file=@-;filename=stdin.txt" -T - https://example.com/upload`

- 静默模式（不显示进度）：
  `curl -s {{URL}}`

- 跳过 SSL 证书验证：
  `curl -k {{URL}}`
