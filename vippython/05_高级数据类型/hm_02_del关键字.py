name_list = ["张三","李四","王五"]
# del关键字删除列表元素
# 日常开发中,要从列表中删除数据,建议使用列表的方法-
del name_list[1]

print(name_list)
name = "张三"
del name
print(name)
# del关键字本质上是将一个变量从内存中删除
# 后续代码就不能使用这个变量了