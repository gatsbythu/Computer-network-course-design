1.	import socket  
2.	import time  
3.	# 客户端配置  
4.	SERVER_IP = '10.0.2.4'  # 虚拟机的IP地址  
5.	SERVER_PORT = 8080  # 服务器监听的端口号  
6.	BUFFER_SIZE = 2048  # 接收缓冲区的大小，单位为字节  
7.	TIMEOUT = 0.1  # 超时时间100ms  
8.	  
9.	# 创建UDP套接字  
10.	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
11.	# 设置套接字超时时间  
12.	client_socket.settimeout(TIMEOUT)  
13.	  
14.	# 初始化统计变量  
15.	received_count = 0  # 接收到的响应数  
16.	total_rtt = 0  # 总的往返时间  
17.	rtt_list = []  # 存储每个请求的往返时间  
18.	  
19.	# 发送12个请求  
20.	for i in range(1, 13):  
21.	    # 构造请求消息  
22.	    seq_no = i.to_bytes(2, 'big')  # 序列号，2字节  
23.	    ver = (2).to_bytes(1, 'big')  # 版本号，1字节，固定为2  
24.	    content = b'Client Request'  # 消息内容  
25.	    message = seq_no + ver + content  # 完整的消息  
26.	  
27.	    # 记录发送时间  
28.	    start_time = time.time()  
29.	    # 发送消息到服务器  
30.	    client_socket.sendto(message, (SERVER_IP, SERVER_PORT))  
31.	    print(f"Sent message: Seq={i}")  
32.	  
33.	    try:  
34.	        # 等待接收响应  
35.	        response, _ = client_socket.recvfrom(BUFFER_SIZE)  
36.	        # 记录接收时间  
37.	        end_time = time.time()  
38.	  
39.	        # 解析响应消息  
40.	        res_seq_no = int.from_bytes(response[:2], 'big')  # 响应的序列号  
41.	        res_ver = int.from_bytes(response[2:3], 'big')  # 响应的版本号  
42.	        res_content = response[3:]  # 响应的内容  
43.	  
44.	        # 计算往返时间（RTT）  
45.	        rtt = (end_time - start_time) * 1000  # 转换为毫秒  
46.	        rtt_list.append(rtt)  # 将RTT添加到列表中  
47.	        total_rtt += rtt  # 累加RTT  
48.	  
49.	        print(f"Received response: Seq={res_seq_no}, RTT={rtt:.2f} ms, Content={res_content.decode()}")  
50.	        received_count += 1  # 增加接收到的响应计数  
51.	    except socket.timeout:  
52.	        # 如果在超时时间内没有接收到响应，打印超时信息  
53.	        print(f"Sequence {i}, request time out")  
54.	  
55.	# 关闭套接字  
56.	client_socket.close()  
57.	  
58.	# 打印汇总信息  
59.	if received_count > 0:  
60.	    max_rtt = max(rtt_list)  # 最大RTT  
61.	    min_rtt = min(rtt_list)  # 最小RTT  
62.	    avg_rtt = total_rtt / received_count  # 平均RTT  
63.	    std_dev_rtt = (sum((x - avg_rtt) ** 2 for x in rtt_list) / received_count) ** 0.5  # RTT标准差  
64.	else:  
65.	    max_rtt = min_rtt = avg_rtt = std_dev_rtt = 0  
66.	  
67.	print(f"\nSummary:")  
68.	print(f"Received UDP packets: {received_count}")  
69.	print(f"Packet loss rate: {(12 - received_count) / 12:.2%}")  
70.	print(f"Max RTT: {max_rtt:.2f} ms")  
71.	print(f"Min RTT: {min_rtt:.2f} ms")  
72.	print(f"Avg RTT: {avg_rtt:.2f} ms")  
73.	print(f"RTT Std Dev: {std_dev_rtt:.2f} ms")  
