from socket import *

HOST = 'localhost' #目的地主机名
PORT = 3555      #目的地端口号
BUFSIZ = 1024       #缓存区大小
ADDR = (HOST, PORT) #UPD用这样的二元组标识套接字
udpClientSocket = socket(AF_INET, SOCK_DGRAM) #创建套接字对象
while True:
    try:
        data = input('>') #输入要发送的数据
        print('send the data: ' + data)
        msg = data.encode('utf-8') #转发为UTF-8编码，防止出现乱码

        # 发送数据:
        udpClientSocket.sendto(msg, ADDR) #把msg发送给ADDR
        # 接收数据:
        print('receive the reply: ' + udpClientSocket.recv(BUFSIZ).decode('utf-8'))
    except Exception as e:
        print(e)

udpClientSocket.close()
