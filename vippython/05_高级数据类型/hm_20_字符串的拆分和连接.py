poem_str = "登鹳雀楼\t王之涣\t白日依山尽\r黄河入海流\r\t欲穷千里目\t更上一层楼"
print(poem_str)
# 拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 连接字符串
new_str = "\n".join(poem_list)
print(new_str)