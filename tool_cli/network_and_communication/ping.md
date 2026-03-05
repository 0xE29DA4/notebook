# ping

> 向网络主机发送 ICMP ECHO_REQUEST 数据包。
> 更多信息：<https://manned.org/ping>

- ping 指定主机：
  `ping {{主机名或IP}}`

- 限制发送包的数量：
  `ping -c {{次数}} {{主机名或IP}}`

- 设置发送间隔（秒）：
  `ping -i {{秒数}} {{主机名或IP}}`

- 设置超时时间：
  `ping -W {{秒数}} {{主机名或IP}}`

- 持续 ping 直到中断（Ctrl+C）：
  `ping {{主机名或IP}}`

- 设置发送包的大小：
  `ping -s {{字节数}} {{主机名或IP}}`

- 洪水式 ping（快速发送）：
  `ping -f {{主机名或IP}}`

- 设置 TTL（生存时间）值：
  `ping -t {{TTL值}} {{主机名或IP}}`
