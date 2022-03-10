import requests

url = "https://fanyi.baidu.com/sug"
s = input("请输入要翻译的单词")
data1 = {
    "kw": s
}
resp = requests.post(url, data=data1)
#   print(resp.text)
print(resp.json())