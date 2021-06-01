# from socket import *
# HOST = '192.168.1.101'
# PORT = 4421
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)
# while True:
#   data = input('请输入待发送的数据： ')
#   if not data:
#     break
#   tcpCliSock.send(data.encode('utf-8'))
#   data1 = tcpCliSock.recv(BUFSIZ)
#   if not data1:
#     break
#   print ('从服务器接收到的结构为：'+data1)
# tcpCliSock.close()


import socket
import sys
IP = 'localhost'  # 填写服务器端的IP地址
port = 4421  # 端口号必须一致
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建套接字
try:
    s.connect((IP, port))   #与服务器建立连接，3次握手
except Exception as e:  #若没有连接成功，则退出
    print(e)
    print('服务器没有找到或未打开！')
    sys.exit()
while True:         #连接成功
    try:
        trigger = input("请输入待发送的数据：(exit-退出)") #输入要发送的数据
        if trigger=='exit':
            break
        s.sendall(trigger.encode()) #发送数据给服务器
        data = s.recv(1024)         #从TCP的另一端（服务器)接收数据
        data = data.decode()
        print('从服务器接收到的结果为：', data) #输出接收到的数据
    except Exception as e:
        print(e)

s.close()