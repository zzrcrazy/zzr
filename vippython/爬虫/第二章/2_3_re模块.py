import re

# finditer:匹配字符串中所有内容,返回的迭代器,从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+", "我的电话是10086,我女朋友的电源是:10010")
# for i in it:
#     print(i.group())
#
# # findall:匹配字符串中所有内容返回的是list,数据多的时候效率不高
# lst = re.findall(r"\d+","我的电话是10086,我女朋友的电源是:10010")
# print(lst)
#
# # search,找到一个结果就返回,返回的结果是match对象,拿数据需要.group
# s = re.search(r"\d+","我的电话是10086,我女朋友的电源是:10010")
# print(s.group())
#

# match匹配第一个
s = re.match(r"\d+","10086,我女朋友的电源是:10010")
print(s.group())

#   预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话是10086,我女朋友的电源是:10010")

for i in ret:
    print(i.group())


#   re.S 让.能匹配换行符
#   (?P<分组名字>正则)可以单独从正则匹配的内容中进一步提取内容




