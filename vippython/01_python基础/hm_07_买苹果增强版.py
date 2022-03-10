# 1.输入苹果单价
price_str = input("苹果单价:")

# 2.输入苹果的重量
weight_str = input("苹果的重量")

# 3.计算并且输出付款金额 但以上两个变量均为字符串
# 注意两个字符串之间不能用乘法
# money = price_str * weight_str
# 将价格转化成小数
price = float(price_str)
# 将重量转化为小数
weight = float(weight_str)
# 用两个小数计算最终金额
money = price * weight
print(money)