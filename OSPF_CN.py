def dijkstra(packets,node_route):  #Dijkstra算法
    table = []  #节点node_route的路由表
    for key in packets[node_route]:  #初始化table
        if(packets[node_route][key]!=float('Inf')):
            row=[key,packets[node_route][key],key,False]
        else:
            row=[key,packets[node_route][key],'无',False]
        table.append(row)
    count=0
    while count<len(table):
        temp=0  #temp用于保存当前table中距离最小的下标
        min=float('Inf')  #min用于记录当前的距离最小值
        for i in range(len(table)):
            if(table[i][3]==False and table[i][1]<min):
                min=table[i][1]
                temp=i
        table[temp][3]=True  #把temp对应的节点加入到已经找到的最短路径的集合中
        count=count+1
        for i in range(len(table)):
            if(table[i][3]==False and packets[table[temp][0]][table[i][0]]!=float('Inf') and (table[temp][1]+packets[table[temp][0]][table[i][0]]<table[i][1])):
                #如果新得到的边可能影响其它未访问的节点，那就更新它的最短距离和下一跳路由器
                table[i][1]=table[temp][1]+packets[table[temp][0]][table[i][0]]
                table[i][2]=table[temp][2]
    table.sort(key=lambda x:x[0])
    return table

def main():
    packets={}  #所有的链路状态分组
    nodes=[]  #所有的节点
    node=input('请输入节点，以#结束：')
    while node!='#':
        if(node not in nodes):
            nodes.append(node)
        else:
            print('节点%s的链路状态分组已存在！' % node)
            node = input('请输入节点，以#结束：')
            continue
        per={}
        row=input('请输入节点%s的链路状态分组(相邻路由器，度量)，以空格隔开，以*结束：' % node)
        while row!='*':
            row=row.split()  #以空格分割输入的字符串
            row=[int(x) if x.isdigit() == True else x for x in row]  #把度量置为整型
            if(row[1]<=0):  #检查输入是否合理
                print('输入违规！')
                row = input('请输入节点%s的链路状态分组(相邻路由器，度量)，以空格隔开，以*结束：' % node)
                continue
            if(row[0] in per):  #避免重复
                print('节点%s的链路状态分组中已有此项！' % node)
                row = input('请输入节点%s的链路状态分组(相邻路由器，度量)，以空格隔开，以*结束：' % node)
                continue
            per[row[0]]=row[1]  #向节点node的链路状态分组中添加表项
            row = input('请输入节点%s的链路状态分组(相邻路由器，度量)，以空格隔开，以*结束：' % node)
        packets[node]=per  #向所有的链路状态分组中添加节点node的链路状态分组
        node = input('请输入节点，以#结束：')
    #将与每一节点未直接相邻的节点的度量置为无穷大（自身除外）
    for key in packets:
        for i in nodes:
            if(i!=key and (i not in packets[key].keys())):
                packets[key][i]=float('Inf')
    while True:
        node_route = input('请输入你想查看路由表的节点：')
        table=dijkstra(packets,node_route)
        print('节点%s的路由表如下:' % node_route)
        print('目的网络  距离  下一跳路由器')
        for row in table:
            print('   '+row[0]+'      '+str(row[1])+'       '+row[2])
if __name__ == '__main__':
    main()