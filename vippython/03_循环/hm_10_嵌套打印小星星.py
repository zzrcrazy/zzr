row = 1
while row <= 5:
    # 每一行打印的* 与行数一致
    # 增加一个小循环 ,专门负责当前行,每一列的星星显示
    # 定义一个列的计数器变量
    col = 1
    while col <= row:
       # print("%d" % col)
        print("*",end="")
        col +=1
    print("")
    row +=1
