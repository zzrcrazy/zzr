name = "小明"
def say_hello():
    """打招呼"""
    print("hello1")
    print("hello2")
    print("hello3")

print(name)
# 只有在函数中主动调用函数才会让函数执行
say_hello()
print(name)