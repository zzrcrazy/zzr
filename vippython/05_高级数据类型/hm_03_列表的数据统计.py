name_list = ["张三","李四","王五"]

# len 函数可以统计列表中函数的总数
list_len = len(name_list)
print("这个列表中有 %d 个元素" % list_len)

# count函数可以统计列表中某一个函数出现的次数
count = name_list.count("张三")
print("张三出现了 %d 次" % count)

# 从列表中删除第一次出现的数据 如果数据不存在  程序会爆错
name_list.remove("张三")
print(name_list)