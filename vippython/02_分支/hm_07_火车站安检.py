has_tickets = True
knife_length = 10

if has_tickets:
    print("请进")
    if knife_length > 20:
        print("你携带的刀太长了,有%d长" % knife_length)
        print("不允许上车")
    else:
        print("安检已经通过,祝你旅途愉快")

else:
    print("不好意思,请先买票")