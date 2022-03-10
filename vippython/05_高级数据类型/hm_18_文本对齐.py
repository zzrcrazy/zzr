# 顺序且居中对齐
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.center(8, "　"))
# ljust 向左对齐  rjust 向右对齐  center 居中对齐
