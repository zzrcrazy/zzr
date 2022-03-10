# 计算0-100之间所有数字的累计求和结果
# 定义最终结果变量
result = 0
# 1.定义一个整数的变量记录循环次数
i = 0
# 2.循环开始
while i <= 100:
    #print(i)
    result += i
    i +=1
print(result)