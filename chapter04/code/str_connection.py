import requests

s1 = "introduce:"
s2 = requests.get("https://www.baidu.com")
text = s2.text
res = s1 + text

print(s2, res)
