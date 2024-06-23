1.	import socket  
2.	import random  
3.	import time  
4.	  
5.	# 服务器配置  
6.	SERVER_IP = '0.0.0.0'  # 监听所有接口  
7.	SERVER_PORT = 8080  
8.	BUFFER_SIZE = 2048  
9.	  
10.	# 创建UDP套接字  
11.	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
12.	server_socket.bind((SERVER_IP, SERVER_PORT))  
13.	  
14.	print(f"UDP server is up and listening at {SERVER_IP}:{SERVER_PORT}")  
15.	  
16.	while True:  
17.	    message, client_address = server_socket.recvfrom(BUFFER_SIZE)  
18.	    seq_no, ver, content = message[:2], message[2:3], message[3:]  
19.	    print(f"Received message from {client_address}: Seq={int.from_bytes(seq_no, 'big')}, Ver={int.from_bytes(ver, 'big')}, Content={content.decode()}")  
20.	  
21.	    if random.choice([True, False]):  
22.	        response = seq_no + ver + b'Server Response'  
23.	        time.sleep(random.uniform(0, 0.1))  # 随机延迟回复  
24.	        server_socket.sendto(response, client_address)  
25.	        print(f"Responded to {client_address} with Seq={int.from_bytes(seq_no, 'big')}")  
26.	    else:  
27.	        print(f"Packet from {client_address} dropped (simulated)")  
