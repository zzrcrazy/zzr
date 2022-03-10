name_list =["zhangsan", "lisi", "wangwu"]

# 取值和取索引()
print(name_list[0])
# 知道数据内容,想知道索引位置
print(name_list.index("lisi"))


# 2.修改
name_list[1] = "zhangzhongrui"
# 列表索引指定的超出范围 会爆错
# name_list[3] = "xiixhaha"
print(name_list.index("zhangzhongrui"))



# 3.增加数据
# append可以在列表的末尾添加数据
name_list.append("王小二")
# inesrt可以在指定的位置添加数据
name_list.insert(1, "小妹妹")
# extend 方法可以将其他列表中的完整内容增加到当前列表的末尾
tem_list = ["孙老大","猪二哥","傻三弟"]
name_list.extend(tem_list)


# 4. 删除
# remove方法从列表删除指定数据
name_list.remove("wangwu")
# pop方法默认把最后一个元素删除
name_list.pop()
# pop方法可以哦指定删除元素的索引
name_list.pop(3)
# clear可以清空列表
name_list.clear()
print(name_list)
