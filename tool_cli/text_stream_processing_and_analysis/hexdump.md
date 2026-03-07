# hexdump

> 以十六进制、十进制、八进制或 ASCII 格式显示文件内容。
> 更多信息：<https://manned.org/hexdump>

- 以十六进制和 ASCII 显示文件：
  `hexdump -C {{文件名}}`

- 以十六进制格式显示文件：
  `hexdump {{文件名}}`

- 以八进制格式显示文件：
  `hexdump -o {{文件名}}`

- 以十进制格式显示文件：
  `hexdump -d {{文件名}}`

- 显示文件的偏移地址：
  `hexdump -x {{文件名}}`

- 只显示 ASCII 字符：
  `hexdump -c {{文件名}}`

- 显示指定字节数：
  `hexdump -n {{字节数}} {{文件名}}`

- 从指定偏移量开始显示：
  `hexdump -s {{偏移量}} {{文件名}}`

- 使用自定义格式显示：
  `hexdump -e '"%08.8_ax  "' -e '4/4 "%08x " "\n"' {{文件名}}`

- 以十六进制和 ASCII 显示，每组 4 字节：
  `hexdump -C -n {{字节数}} {{文件名}}`

- 显示文件的二进制内容：
  `hexdump -v -e '"%08.8_ax  "' -e '8/1 "%02x " "\n"' {{文件名}}`

- 显示可打印字符：
  `hexdump -v -e '"%_ad #"' -e '1/1 "%_p" "\n"' {{文件名}}`

- 以十六进制显示，每行 16 字节：
  `hexdump -v -e '"%08.8_ax  "' -e '16/1 "%02x " "\n"' {{文件名}}`

- 显示文件的十六进制转储并保存：
  `hexdump -C {{文件名}} > {{输出文件}}`

- 显示文件的指定范围：
  `hexdump -s {{起始偏移}} -n {{字节数}} {{文件名}}`

- 以不同进制混合显示：
  `hexdump -e '"%08.8_ax  "' -e '4/4 "%08x " "\n"' {{文件名}}`

- 显示文件的十六进制和 ASCII，跳过空格：
  `hexdump -C {{文件名}} | grep -v "^0"`

- 以二进制格式显示：
  `hexdump -v -e '"%08.8_ax  "' -e '8/1 "%08b " "\n"' {{文件名}}`

- 显示文件的十六进制，每字节一行：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " "\n"' {{文件名}}`

- 显示文件的十六进制和 ASCII，高亮显示特定字节：
  `hexdump -C {{文件名}} | grep --color=auto {{模式}}`

- 以十六进制显示，显示字节偏移：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " "\n"' {{文件名}}`

- 显示文件的十六进制，每 8 字节一组：
  `hexdump -v -e '"%08.8_ax  "' -e '8/1 "%02x " "\n"' {{文件名}}`

- 以十六进制和 ASCII 显示，只显示非零字节：
  `hexdump -C {{文件名}} | grep -v " 00 \|00 \| 00$"`

- 显示文件的十六进制，显示字节计数：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " " " "%_p" "\n"' {{文件名}}`

- 以十六进制显示，显示行号：
  `hexdump -v -e '"%08.8_ax  "' -e '16/1 "%02x " "\n"' {{文件名}}`

- 显示文件的十六进制和 ASCII，显示字节位置：
  `hexdump -C {{文件名}} | nl`

- 以十六进制显示，显示字符编码：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " " " "%_u" "\n"' {{文件名}}`

- 显示文件的十六进制，显示控制字符：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " " " "%_c" "\n"' {{文件名}}`

- 以十六进制显示，显示字节统计：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " "\n"' {{文件名}} | wc -l`

- 显示文件的十六进制，显示字频率：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | sort | uniq -c | sort -nr`

- 以十六进制显示，显示非打印字符：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " " " "%_p" "\n"' {{文件名}} | grep -E '[^ -~]'

- 显示文件的十六进制，显示字节模式：
  `hexdump -v -e '"%08.8_ax  "' -e '16/1 "%02x " "\n"' {{文件名}} | grep -E '({{模式}})'

- 以十六进制显示，显示字节差异：
  `hexdump -C {{文件1}} > {{输出1}} && hexdump -C {{文件2}} > {{输出2}} && diff {{输出1}} {{输出2}}`

- 显示文件的十六进制，显示重复行：
  `hexdump -C {{文件名}} | uniq -d`

- 以十六进制显示，显示字节偏移量：
  `hexdump -v -e '"%08.8_ax  "' -e '1/1 "%02x " "\n"' {{文件名}} | awk '{print $1}'

- 显示文件的十六进制，显示字节值：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | sort -u`

- 以十六进制显示，显示字节分布：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | sort | uniq -c | awk '{print $2, $1}'`

- 显示文件的十六进制，显示字节范围：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | sort -n | head -1; hexdump -v -e '1/1 "%02x\n"' {{文件名}} | sort -n | tail -1`

- 以十六进制显示，显示字节直方图：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | sort | uniq -c | awk '{printf "%02x: %d\n", $1, $2}'

- 显示文件的十六进制，显示字节模式匹配：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | grep -E '({{模式}})'

- 以十六进制显示，显示字节熵：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | sort | uniq -c | awk '{sum+=$2} END{for(i=0;i<=255;i++) count[i]=0; for(i in count) if(count[i]>0) p=count[i]/sum; entropy-=p*log(p)/log(2)} END{print "Entropy:", entropy}'

- 显示文件的十六进制，显示字节校验和：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | awk '{sum+=$1} END{printf "Checksum: %04x\n", sum%65536}'

- 以十六进制显示，显示字节 XOR：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | awk '{xor=xor^$1} END{printf "XOR: %02x\n", xor}'

- 显示文件的十六进制，显示字节 AND：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | awk '{if(NR==1) and=$1; else and=and&$1} END{printf "AND: %02x\n", and}'

- 以十六进制显示，显示字节 OR：
  `hexdump -v -e '1/1 "%02x\n"' {{文件名}} | awk '{or=or|$1} END{printf "OR: %02x\n", or}'

- 显示文件的十六进制，显示字节平均值：
  `hexdump -v -e '1/1 "%d\n"' {{文件名}} | awk '{sum+=$1; count++} END{printf "Average: %.2f\n", sum/count}'

- 以十六进制显示，显示字节中位数：
  `hexdump -v -e '1/1 "%d\n"' {{文件名}} | sort -n | awk '{if(NR%2==1) median=$1; else median=(prev+$1)/2} {prev=$1} END{printf "Median: %d\n", median}'

- 显示文件的十六进制，显示字节标准差：
  `hexdump -v -e '1/1 "%d\n"' {{文件名}} | awk '{sum+=$1; sumsq+=$1*$1; count++} END{mean=sum/count; printf "StdDev: %.2f\n", sqrt(sumsq/count - mean*mean)}'

- 以十六进制显示，显示字节方差：
  `hexdump -v -e '1/1 "%d\n"' {{文件名}} | awk '{sum+=$1; sumsq+=$1*$1; count++} END{mean=sum/count; printf "Variance: %.2f\n", sumsq/count - mean*mean}'