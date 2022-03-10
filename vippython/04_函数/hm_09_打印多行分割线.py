def print_line(char,time):
    print(char * time)

def print_lines(char,times):
    """"""
    row = 0
    while row < 5:
        print(char * times)
        row += 1

print_lines("-", 20)