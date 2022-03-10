i = 0
while i <= 10:
    if i == 3:
        # 在循环中,若果使用continue 这个关键字
        # 在使用关键字前,需要确认循环的计数是否修改
        # 否则可能会导致死循环
        i += 1
        continue
    print(i)
    i += 1

