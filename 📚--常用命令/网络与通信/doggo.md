# doggo

> dig 的现代化替代品，更友好的 DNS 查询工具。
> 更多信息：<https://github.com/mr-karan/doggo>

- 查询域名的 A 记录：
  `doggo {{域名}}`

- 查询特定类型的 DNS 记录（如 A, AAAA, MX, NS, TXT）：
  `doggo {{域名}} {{MX}}`

- 指定 DNS 服务器：
  `doggo {{域名}} @{{8.8.8.8}}`

- 使用 JSON 格式输出：
  `doggo {{域名}} --json`

- 显示详细的 DNS 响应：
  `doggo {{域名}} --time`

- 反向 DNS 查询（IP 到域名）：
  `doggo -x {{IP地址}}`

- 查询所有类型的记录：
  `doggo {{域名}} ANY`

- 指定传输协议（UDP, TCP, DoT, DoH）：
  `doggo {{域名}} --protocol {{DoH}}`
