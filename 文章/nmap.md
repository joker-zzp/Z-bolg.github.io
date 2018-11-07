# Nmap 命令使用

## 探测主机存活常用方法

### -sP

-sP : 进行ping扫描，做出响应的主机，不做进一步测试

`nmap -sP 192.168.0.0/24 `

### -sn

-sn:  Ping Scan - disable port scan  #ping探测扫描主机， 不进行端口扫描 （测试过对方主机把icmp包都丢弃掉，依然能检测到对方开机状态）

`nmap -sn 192.168.0.100-255 `

### -sA

-sA : 发送tcp的ack包进行探测，可以探测主机是否存活

`nmap 192.168.0.100 -sA `

## 端口扫描的高级用法

### -sS

-sS : 半开放扫描（非3次握手的tcp扫描）

> 使用频率最高的扫描选项：SYN扫描,又称为半开放扫描，它不打开一个完全的TCP连接，执行得很快，效率高  
> 一个完整的tcp连接需要3次握手，而-sS选项不需要3次握手  
> Tcp SYN Scan (sS) 它被称为半开放扫描  
> 优点：Nmap发送SYN包到远程主机，但是它不会产生任何会话，目标主机几乎不会把连接记入系统日志。（防止对方判断为扫描攻击），扫描速度快，效率高，在工作中使用频率最高  
> 缺点：它需要root/administrator权限执行

`nmap -sS 192.168.0.100 `

### -sT

-sT : 3次握手方式tcp的扫描

> Tcp connect() scan (sT)和上面的Tcp SYN 对应，TCP connect()扫描就是默认的扫描模式.  
> 不同于Tcp SYN扫描,Tcp connect()扫描需要完成三次握手,并且要求调用系统的connect().  
> 优点：你勿需root权限。普通用户也可以使用.  
> 缺点：这种扫描很容易被检测到，在目标主机的日志中会记录大批的连接请求以及错误信息，由于它要完成3次握手，效率低，速度慢，建议使用-sS.  

`nmap -sT 192.168.0.100 `

`nmap 192.168.0.100 `

### -sU

-sU : Udp scan(sU) 顾名思义,这种扫描技术用来寻找目标主机打开的UDP端口.它不需要发送任何的SYN包，因为这种技术是针对UDP端口的。UDP扫描发送UDP数据包到目标主机，并等待响应,
如果返回ICMP不可达的错误消息，说明端口是关闭的，如果得到正确的适当的回应，说明端口是开放的.udp端口扫描速度比较慢

`nmap -sU 192.168.0.100 `

### -sF

-sF : 也是tcp的扫描一种，发送一个FIN标志的数据包

> FIN scan(sF)
有时候TcpSYN扫描不是最佳的扫描模式,因为有防火墙的存在.目标主机有时候可能有IDS和IPS系统的存在,防火墙会阻止掉SYN数据包。发送一个设置了FIN标志的数据包并不需要完成TCP的握手.
和sS扫描效果差不多，比sT速度快

`nmap -sF 192.168.0.100 `

### -sF、-sX、-sN

> 秘密FIN数据包扫描、圣诞树(XmasTree)、空(Null)扫描模式  
> 有的防火墙可能专门阻止-sS扫描。使用这些扫描可以发送特殊标记位的数据包  
> 比如，-sF发送一个设置了FIN标志的数据包  
> 和sS扫描效果差不多，都比sT速度快
> 除了探测报文的标志位不同，三种扫描在行为上一致
> 优势：能躲过一些无状态防火墙和报文过滤路由器，比SYN还要隐秘  
> 劣势：现代的IDS产品可以发现，并非所有的系统严格遵循RFC 793  

> 即使SYN扫描都无法确定的情况下使用：一些防火墙和包过滤软件能够对发送到被限制端口的SYN数据包进行监视，而且有些程序比如synlogger和courtney能够检测那些扫描。使用-sF、-sX、-sN可以逃过这些干扰。  
> 这些扫描方式的理论依据是：关闭的端口需要对你的探测包回应RST包，而打开的端口必需忽略有问题的包。  
> FIN扫描使用暴露的FIN数据包来探测，而圣诞树扫描打开数据包的FIN、URG和PUSH标志。  
> 由于微软决定完全忽略这个标准，另起炉灶。所以这种扫描方式对Windows无效。  
> 不过，从另外的角度讲，可以使用这种方式来分别两种不同的平台。  
> 如果使用这种扫描方式可以发现打开的端口，你就可以确定目标注意运行的不是Windows系统。  
> 如果使用-sF、-sX或者-sN扫描显示所有的端口都是关闭的，而使用-sS（SYN）扫描显示有打开的端口，你可以确定目标主机可能运行的是Windwos系统。  
> 现在这种方式没有什么太大的用处，因为nmap有内嵌的操作系统检测功能。还有其它几个系统使用和windows同样的处理方式，包括Cisco、BSDI、HP/UX、MYS、IRIX。  
> 在应该抛弃数据包时，以上这些系统都会从打开的端口发出复位数据包。  

### -sW

-sW : Window扫描，即窗口扫描

当然也可以利用Window扫描方式，得出一些端口信息，可以与之前扫描分析的结果相互补充。Window扫描方式只对某些TCPIP协议栈才有效。
它也是基于tcp的扫描

`nmap -sW 192.168.0.100 `


### -sV

-sV : 版本检测

版本检测是用来扫描目标主机和端口上运行的软件的版本，如下扫描，多出了ssh的版本信息

`nmap -sV 192.168.0.100 `

## nmap 扫描计划

+ 获取IP
    - host 网址
    - host 域名
    - dig 域名
+ 是否存活
    - ping IP
    - nmap -sP --script discovery IP
+ 扫描在线主机
    - nmap -sP 192.168.0.*
+ 探测IP协议
    - nmap -PO IP
+ 获取系统概况
    - nmap -A IP
+ 探测防火墙 
    - 探测是否有防火墙 nmap -PN IP
    - 探测防火墙规则 nmap -sA IP
    - TCP Windows扫描 nmap -sW IP
    - FIN 扫描 nmap -sF IP # FIN扫描方式用于识别端口是否关闭，收到RST回复说明该端口关闭，否则说明open或filtered状态
+ TCP扫描
    - nmap -sT -p- -Pn IP
    - nmap -sT -p- 192.168.0.1-254 # 所有子网TCP扫描，费时
    - nmap -sL 192.168.0.0/24
+ SYN扫描
    - nmap -sS -p- -Pn IP
+ UDP扫描
    - nmap -sU IP # UDP扫描费时，所以去掉-p-，默认扫描
+ Xmas扫描
    - nmap -sX -p- -Pn IP
+ Null扫描
    - nmap -sN -p- -Pn IP
+ 绕开鉴权
    - nmap --script=auth 192.168.0.*
+ 探测操作系统
    - nmap -O IP
+ 探测软件版本
    - nmap -V IP
    - nmap -sTV -p- -Pn IP
+ 探测局域网内更多服务
    - nmap -n --script=broadcast IP
+ 碎片化
    - nmap -f IP
    - nmap --mtu 16 IP
+ 诱饵
    - nmap -D RND:10 TARGET
    - nmap -D decop1,decop2,decop3 target
+ MAC地址欺骗
    - nmap -sT -PN -spoof-mac aa:bb:cc:dd:ff target
    - nmap -spoof-mac Scisio IP # -spoof-mac可以根据厂商名字伪造不同mac地址
+ 发送间隔时间控制
    - nmap -scan_delay 5ms IP
+ 发送错误校验
    - nmap --badsum target
+ Http方法
    - nmap -p 80,443 -script http-methods scanme.nmap.org
+ 发现文件
    - nmap -sV --script http-enum IP
+ 判断是否使用默认端口
    - nmap -sV --script=smtp-strangeport IP
+ 利用第三方数据库
    - nmap --script external IP
+ 获取PHP版本信息
    - nmap -sV --script=http-php-version IP
    - 如果想对一个基于wordPress的web站点进行渗透测试，可以使用一下脚本
        1. http-wordpress-plugins
        2. http-wordpress-enum
        3. http-wordpress-brute
+ 用户发现IP地址黑名单
    - nmap -sn IP --script dns-blacklist
+ 简单暴力猜解
    - nmap --script=brute 192.168.0.*
+ 检测是否存在漏洞
    - nmap --script=vuln 192.168.0.*
+ 按应用服务扫描
    - vnc 扫描
        * 检查vnc bypass nmap --script=realvnc-auth-bypass IP
        * 检查vnc 认证方式 nmap --script=vnc-auth IP
        * 获取vnc 信息 nmap --script=vnc-info IP
    - smb 扫描
        * smb 破解 nmap --script=smb-brute.nse IP
        * smb 字典破解 nmap --script=smb-brute.nse --script-arge=userdb=/var/passwd,passdb=/var/passwd IP
        * smb 已知几个严重漏洞 nmap --script=smb-check-vulns.nse --script-args=unsafe=1 IP
        * 查看共享目录 nmap -p 445 --script smb-ls --script-arge\`share=e$,path=\,smbuser=test,smbpass=test\` IP
        * 查询主机一些敏感信息 nmap -p 445 -n --script=smb-psexec --script-args=smbuser=test,smbpass=test IP
        * 查看回话 nmap -n -p 445 --script=smb-enum-sessions.nse --script-args=smbuser=test,smbpass=test IP
        * 系统信息 nmap -n -p 445 --script=smb-os-discovery.nse --script-args=smbuser=test,smbpass=test IP
    - Mssql 扫描
        * 猜解mssql 用户名密码 nmap -p 1433 --script=ms-sql-brute --script-args=userdb=/var/passwd,passdb=/var/passwd IP
        * xp_cmdshell 执行命令 nmap -p 1433 --script=ms-sql-xp-cmdshell --script-args mssql.username=sa,mssql.password=sa,ms-sql-xp-cmdshell.cmd="net user" IP
        * dumphash 值 nmap -p 1433 --script=ms-sql-dump-hashes.nse --script-args mssql.username=sa,mssql.password=sa IP
    - Mysql 扫描
        * 扫描root 口令 nmap -p 3306 --script=mysql-empty-password.nse IP
        * 列出所有mysql 用户 nmap -p 3306 --script=mysql-user.nse --script-ages=mysqluser=root IP
        * 支持同一应用的所有扫描 nmap --script=mysql-* IP
    - Oracle 扫描
        * oracle sid 扫描 nmap --script=oracle-sid-brute -p 1521-1560 IP
        * oracle 弱口令破解 nmap --script=oracle-brute -p 1521 --script-ages oracle-brute.sid=ORCL,userdb=/var/passwd,passdb=/var/passwd IP
+ 其他一些比较好用的脚本
    - 发现网关
        * nmap --script=broadcast-netbios-master-browser IP
    - telnet 破解
        * nmap -sV --script=telnet-brute IP
    - dos 攻击
        * nmap --script http-slowloris --max-parallelism 400 IP
    - 破解rsync
        * nmap -p 873 --script=rsync-brute --script-ages 'rsync-brute.module=www' IP
    - informix 数据库破解
        * nmap -p 9088 --script=informix-brute IP
    - pgsql 破解
        * nmap -p 5432 --script=pgsql-brute IP
    - snmap 破解
        * nmap -sU --script=snmp-brute IP
    - 检查http 方法
        * nmap --script=http-methods.nse IP







