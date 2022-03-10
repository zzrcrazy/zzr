# 计算0-100之间所有偶数和
i = 0
result = 0
while i <= 100:
    # 判断变量i中数值是否是偶数
    # i%2 ==0
    if i % 2 ==0:
        result +=i
    i += 1
print(result)