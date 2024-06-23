1.	import socket  
2.	  
3.	# 定义一个函数，启动反向 TCP 服务器  
4.	def reverse_tcp_server(host, port):  
5.	    # 创建一个 TCP/IP 套接字对象  
6.	    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
7.	      
8.	    # 绑定套接字到主机地址和端口号  
9.	    server_socket.bind((host, port))  
10.	      
11.	    # 让套接字开始监听传入的连接（最大连接数为 5）  
12.	    server_socket.listen(5)  
13.	    print("Server listening on", host, port)  
14.	  
15.	    # 无限循环，持续接受并处理客户端的连接  
16.	    while True:  
17.	        # 接受客户端的连接，并返回一个新的套接字对象和客户端地址  
18.	        client_socket, addr = server_socket.accept()  
19.	        print('Connected by', addr)  
20.	          
21.	        # 调用函数处理客户端连接  
22.	        handle_client(client_socket)  
23.	  
24.	    # 关闭服务器套接字（这一行实际上永远不会执行，因为前面的 while 循环是无限的）  
25.	    server_socket.close()  
26.	  
27.	# 定义一个函数，用于处理客户端连接  
28.	def handle_client(client_socket):  
29.	    # 无限循环，持续接收并处理来自客户端的消息  
30.	    while True:  
31.	        # 从客户端套接字接收数据（最多 4096 字节）  
32.	        message = client_socket.recv(4096)  
33.	          
34.	        # 如果未接收到任何数据，跳出循环  
35.	        if not message:  
36.	            break  
37.	  
38.	        # 解析消息类型（前 2 字节）  
39.	        message_type = int.from_bytes(message[0:2], 'big')  
40.	        print(f"Received message type: {message_type}")  
41.	  
42.	        # 根据消息类型进行处理  
43.	        if message_type == 1:  # Initialization 报文  
44.	            n = int.from_bytes(message[2:6], 'big')  
45.	            send_agree(client_socket)  
46.	        elif message_type == 3:  # reverseRequest 报文  
47.	            length = int.from_bytes(message[2:6], 'big')  
48.	            data = message[6:6+length].decode()  
49.	            print(f"Received data: {data}")  
50.	            reversed_data = data[::-1]  
51.	            send_reverse_answer(client_socket, reversed_data)  
52.	      
53.	    # 关闭客户端套接字  
54.	    client_socket.close()  
55.	  
56.	# 定义一个函数，发送 agree 报文  
57.	def send_agree(client_socket):  
58.	    message_type = 2  
59.	     
