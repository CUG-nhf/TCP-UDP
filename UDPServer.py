from socket import *
from time import ctime

HOST = ''   #主机名
PORT = 3555 #端口号
BUFSIZ = 1024   #设置缓存区大小为1024字节
ADDR = (HOST, PORT) #UPD用这样的二元组标识套接字

udpServerSocket = socket(AF_INET, SOCK_DGRAM)   #创建套接字对象，UDP客户端
udpServerSocket.bind(ADDR)  #绑定主机与端口

while True:
    try:
        data, addr = udpServerSocket.recvfrom(BUFSIZ)#接收数据
        print('来自主机 %s，端口: %s.' % addr)#打印接收度数据
        print(data.decode('utf-8'))           #打印接收度数据
        reply = 'Hello, this is udpserver!'   #可以看出UDP套接字能读能写，双全工
        udpServerSocket.sendto(reply.encode('utf-8'), addr)#回复客服端 
    except Exception as e:
        print(e)

udpServerSocket.close()

