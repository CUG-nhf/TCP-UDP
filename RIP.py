class Net:
    def __init__(self,DesNet,Dis,NextHoop):
        self.DesNet = DesNet     #目的网络
        self.Dis = Dis       #距离
        self.NextHoop = NextHoop     #下一跳
        self.next = None

class Link:
    # 构造函数
    def __init__(self):
        self.head = Net(None,None,None)            # 头节点为空
        self.tail = self.head
        self.size = 1
    # 添加节点
    def add(self,DesNet,Dis,NextHoop):
        net = Net(DesNet,Dis,NextHoop)        # 创建新节点
        self.tail.next = net                    # 尾节点的下一个节点为新节点
        self.tail = net                         # 尾节点为新节点
        self.size = self.size + 1
    # 插入节点（此节点作为第index个节点）
    def insert(self,DesNet,Dis,NextHoop,index):
        if(index > self.size):
            print('链表还没有这么长哟！请输入小一点的整数......')
        else:
            net = self.head
            insert_net = Net(DesNet,Dis,NextHoop)
            for i in range(index - 1):
                net = net.next                      # 推进到要插入的位置
            insert_net.next = net.next
            net.next = insert_net
            self.size = self.size + 1
    # 删除节点（索引为index）
    def delete(self,index):
        if (index > self.size):
            print('链表还没有这么长哟！请输入小一点的整数......')
        else:
            net = self.head
            for i in range(index - 1):
                net = net.next
            temp = net.next
            net.next = temp.next
            self.size = self.size - 1
    # 改变指定节点的数据
    def change(self,DesNet,Dis,NextHoop,index):
        if (index > self.size):
            print('链表还没有这么长哟！请输入小一点的整数......')
        else:
            net = self.head
            for i in range(index):                  # 推进到要改变节点的位置
                net = net.next
            net.DesNet =DesNet
            net.Dis = Dis
            net.NextHoop =NextHoop
    # 返回节点的数据
    def getData(self,index):
        if(index > self.size):                                  # 判断是否超过链表的长度
            print('链表还没有这么长哟！请输入小一点的整数......')
        else:
            net = self.head
            for i in range(index):
                net = net.next
            return [net.DesNet,net.Dis,net.NextHoop]
    # 返回节点的长度
    def getSize(self):
        return self.size
    def length(self):
        # 获取这个链表的长度
        count = 0
        cur = self._head
        while cur != None:
            count += 1
            cur = cur.next
        return count
def main():
    table=Link()     #初始路由表
    NewTable=Link()       #来自某个路由器的路由表
    FinalTable=Link()      #最终形成的路由表
    temptable1=[]
    temptable2=[]
    a=int(input('请输入初始路由表行数：'))
    print('请输入整个路由表：')
    for i in range(a):
        DesNet,Dis,NextHoop=input().split()
        table.add(DesNet,Dis,NextHoop)
        FinalTable.add(DesNet,Dis,NextHoop)
    print('路由表初始化完成')
    b=input('新路由表来自的路由器：')
    c=int(input('新路由表的行数：'))
    print('请输入新路由表的信息：')
    for i in range(c):
        DesNet,Dis=input().split()
        Dis=int(Dis)+1
        NewTable.add(DesNet,Dis,b)
    for i in range(c):
        if i==0:continue
        count = 0
        for j in range(a):
            if j==0:continue
            temptable1=NewTable.getData(i)
            temptable2=FinalTable.getData(j)
            if temptable1[0]==temptable2[0]:   #如果目标网络相同
                if temptable1[2]==temptable2[2]:   #如果目标网络和下一跳均相同
                    FinalTable.change(temptable1[0],temptable1[1],temptable1[2],j)
                if temptable1[2]!=temptable2[2]:   #如果目标网络一致，下一跳不同
                    if int(temptable1[1]) < int(temptable2[1]):
                        FinalTable.change(temptable1[0], temptable1[1], temptable1[2], j)
                    else:continue
            if temptable1[0]!=temptable2[0]:
                count=count+1
        if int(count)==int(a)-1:
            FinalTable.add(temptable1[0], temptable1[1], temptable1[2])
    print('新的路由表为：')
    print('目的网络    距离    下一跳路由器')
    for i in range(FinalTable.size):
        if i==0:continue
        data = FinalTable.getData(i)
        print(str(data[0]) + '        ' + str(data[1]) + '         ' + str(data[2]))

if __name__=='__main__':
    main()
