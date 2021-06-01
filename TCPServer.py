# import socket
# import time
# MaxBytes=1024
# host ='192.168.1.101'
# port = 4421
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.settimeout(30)
# client.connect((host,port))
# while True:
#     inputData=input();
#     #等待输入数据
#     if(inputData=="quit"):
#         print("我要退出了，再见")
#         break
#     sendBytes = client.send(inputData.encode())
#     if sendBytes<=0:
#         break;
#     recvData = client.recv(MaxBytes)
#     if not recvData:
#         print('接收数据为空，我要退出了')
#         break
#     localTime = time.asctime( time.localtime(time.time()))
#     print(localTime, ' 接收到数据字节数:',len(recvData))
#     print(recvData.decode())
# client.close()
# print("我已经退出了，后会无期")


import socket

host = "localhost"  # 服务器端可以写"localhost"，可以为空字符串""，也为本机IP地址
port = 4421  # 端口号
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建套接字
s.bind((host, port)) #绑定主机名，端口号到套接字上
s.listen(1)     #开始监听，等待连接的最大数为 1
print('服务器已经启动')
conn, addr = s.accept() #接收一个连接
print('', addr)
print('已经建立连接')
while True:
    try:
        data = conn.recv(1024) #从客服端接收数据
        data = data.decode()    
        if not data:
            break
        print('从客户端接收到信息为：', data)
        send = input('给客户端接的回复信息为：')    
        conn.sendall(send.encode()) #发送send给客服端
    except Exception as e:
        print(e)

conn.close()
s.close()
