# DOS 命令

command                        |解释
:------------------------------|:----------------------------
net user 用户名 密码 /add       |创建用户
net user guest /active:yes     |激活guest用户
net user                       |查看有哪些用户
net user 账户名                 |查看账户的属性
net localGroup administrators 用户名 /add |把“用户”添加到管理员中使其具有管理员权限 注意：administrator后加s用复数
net user guest 12345          |用guest用户登录后用将密码改为12345
net password 密码              |更改系统登录密码
net share                      |查看本地开启的共享
net share ipc$                 |开启ipc$共享
net share ipc$ /del            |删除ipc$共享
net share c$ /del              |删除C:共享
netstat -a                     |查看开启了哪些端口，常用netstat -an
netstat -n                     |查看端口的网络连接情况，常用netstart -an
