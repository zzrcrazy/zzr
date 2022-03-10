xiaoming_dict = {"name": "小明"}
# 取值
print(xiaoming_dict["name"])
# 再取值时如果指定的key不存在,程序会报错
# print(xiaoming_dict["name123"])

# 增加/修改
# 如果key不存在会新增键值对  如果存在会进行修改
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "小小明"

# 删除
# xiaoming_dict.pop("name")
xiaoming_dict.pop("name123")   # 不存在的key值删除会报错
print(xiaoming_dict)