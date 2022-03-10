import random

player =int(input("请输入你要出的拳 石头(1)/剪刀(2)/布(3)"))
computer = random.randint(1, 3)
print("玩家选的拳头是%d -电脑出的拳是 %d "% (player, computer))
# 比较胜负

if((player == 1 and computer == 2)
        or (player ==2 and computer == 3)      # 为了保证阅读增加了8个空格
        or (player == 3 and computer == 1)):

    print("欧耶 电脑弱爆了")
# 平局
elif player == computer:
    print("真是心有灵犀啊 我们再来一盘")
else:
    print("我不服,再来")