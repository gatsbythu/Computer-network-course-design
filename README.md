# Computer-network-course-design
项目简介
本项目实现了一个简单的 TCP 客户端和服务器程序。客户端程序从一个 ASCII 文件中读取数据，并将数据分块发送到服务器。服务器接收数据后，反转数据并返回给客户端，客户端打印反转后的数据。

运行环境
操作系统：Windows11
编程语言：Python 3
依赖库：无额外依赖库，仅使用 Python 标准库中的 socket 和 random

配置选项

客户端
server_ip：服务器 IP 地址（例如：10.0.2.4）
server_port：服务器端口号（例如：12345）
file_path：ASCII 文件路径（例如：ascii_file.txt）
lmin 和 lmax：数据块大小范围（例如：10 和 100）

服务器
host：服务器主机地址
port：服务器端口号（例如：12345）

文件列表
reverse_tcp_server.py：服务器端代码
reverse_tcp_client.py：客户端代码
ascii_file.txt：示例 ASCII 文件，包含要发送的数据
readme.txt：本说明文件



UDP Socket 编程任务
1. 简介
本项目通过创建UDP客户端和服务器来模拟网络通信，测量往返时间（RTT）和丢包率。

2. 需求
Python 3
VirtualBox 
基本网络设置，包含主机和虚拟机

3. 文件
udpserver.py: 服务器脚本
udpclient.py: 客户端脚本

4. 运行环境
主机操作系统：支持Python 3的任意操作系统，本机为win11
虚拟机操作系统：支持Python 3的任意Linux发行版

5. 配置
确保网络设置允许主机和虚拟机之间的通信。
禁用主机和虚拟机上的防火墙，以免阻止UDP通信。
