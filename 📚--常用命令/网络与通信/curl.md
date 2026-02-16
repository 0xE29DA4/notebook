# curl

## get

```sh
# 发送 GET 并且输出到文件（指定输出文件名字）
curl -o FILE_OUTPUT URL

# 发送 GET 并且输出到文件
curl -O URL
```

## 查看更详细的交互信息

```sh
# 查看响应头和响应体
curl -i https://httpbin.org/get

# 查看超级详细的通信过程
curl -v https://httpbin.org/get

# 跟随 HTTP 重定向
curl -L http://google.com
```

## 发送数据

```sh
# 发送表单数据
curl -X POST -d "name=Gemini&project=curl-tutorial" https://httpbin.org/post

# 发送文件或表单
# -F 会让 curl 自动设置 Content-Type: multipart/form-data
curl -F "file=@/path/to/your/file.txt" -F "user=test" https://httpbin.org/post

# 发送 json 数据
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "clever-user", "languages": ["Python", "TypeScript", "Rust"]}' \
  https://httpbin.org/post

# 发送一个 PUT 请求来更新资源
curl -X PUT -H "Content-Type: application/json" -d '{"status": "completed"}' https://httpbin.org/put

# 发送一个 DELETE 请求来删除资源
curl -X DELETE https://httpbin.org/delete
```

## 其他功能

```sh
# silent: 不显示进度条或错误信息
curl -s URL
# --insecure: 不验证 SSL 证书
curl -k URL
```
