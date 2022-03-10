row = 1
while row <= 9:
    col = 1
    while col <= row:
        # print(str(col) +" * " + str(row) + " = "+str(row*col),end="   ")
        print("%d * %d = %d" % (col,row,col*row),end="\t")
        col +=1
    print("")
    row +=1
