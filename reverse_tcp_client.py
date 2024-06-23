1.	import socket  
2.	import random  
3.	  
4.	def reverse_tcp_client(server_ip, server_port, file_path, lmin, lmax):  
5.	    # 创建一个 TCP/IP 套接字对象  
6.	    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
7.	      
8.	    # 连接到服务器  
9.	    client_socket.connect((server_ip, server_port))  
10.	  
11.	    def send_initialization(n):  
12.	        # 消息类型为 1（Initialization 报文）  
13.	        message_type = 1  
14.	        # 将消息类型和序列号转换为字节格式并组合成一个消息  
15.	        message = message_type.to_bytes(2, 'big') + n.to_bytes(4, 'big')  
16.	        # 发送消息  
17.	        client_socket.sendall(message)  
18.	  
19.	    def send_reverse_request(data):  
20.	        # 消息类型为 3（reverseRequest 报文）  
21.	        message_type = 3  
22.	        length = len(data)  
23.	        # 将消息类型、数据长度和数据转换为字节格式并组合成一个消息  
24.	        message = message_type.to_bytes(2, 'big') + length.to_bytes(4, 'big') + data.encode()  
25.	        # 发送消息  
26.	        client_socket.sendall(message)  
27.	        # 接收服务器的回复消息  
28.	        reverse_answer = client_socket.recv(4096)  
29.	        # 返回回复消息中的反转数据  
30.	        return reverse_answer[6:].decode()  
31.	  
32.	    # 打开 ASCII 文件并读取数据  
33.	    with open(file_path, 'r') as file:  
34.	        data = file.read()  
35.	  
36.	    # 随机生成数据块的大小  
37.	    chunk_size = random.randint(lmin, lmax)  
38.	    # 分块发送数据并接收反转数据  
39.	    for i in range(0, len(data), chunk_size):  
40.	        chunk = data[i:i + chunk_size]  
41.	        reversed_chunk = send_reverse_request(chunk)  
42.	        print(f'第 {i//chunk_size+1} 块: {reversed_chunk}')  
43.	  
44.	    # 关闭客户端套接字  
45.	    client_socket.close()  
46.	  
47.	# 示例调用  
48.	reverse_tcp_client('10.0.2.4', 12345, 'ascii_file.txt', 10, 100)  
