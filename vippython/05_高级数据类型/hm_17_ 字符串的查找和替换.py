hello_str = "hello world"

# 1,判断是否以指定字符串开始
print(hello_str.startswith("hel"))

# 2,判断是否以指定字符串结束
print(hello_str.endswith("ld"))

# 3,查找指定字符串
# index也可以查找指定字符串在大字符串中的索引
# index方法如果不存在会报错
# find方法如果不存在,会返回-1
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 4,替换字符串
# replace方法执行完成会返回一个新的字符串
# 注意不会修改原有字符串
print(hello_str.replace("world", "python"))

print(hello_str)

