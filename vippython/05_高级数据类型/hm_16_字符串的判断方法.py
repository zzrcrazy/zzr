# 1.判断空白字符
space_str = "  \t\r\n"
print(space_str.isspace())

# 判断字符串只包含数字
# 都不能判断小数
# num_str = "2"
# num_str = "⑴"   # 特殊符号 Unicode
num_str = "一千零一"

print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric()) # 可以判断中文数字