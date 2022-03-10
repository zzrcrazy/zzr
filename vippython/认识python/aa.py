fee = input('请输入午餐费用')
members = input('请输入聚餐人姓名,以英文逗号分隔')
memberlist = members.split(',')
num = len(memberlist)
avgfee = int(fee)/ num
print(avgfee)