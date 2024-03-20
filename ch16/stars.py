#파이썬으로 사이트 정보 읽어오기
# import requests
# url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
# res = requests.get(url) #<class 'dict'>

from matplotlib import pyplot as plt
import json

name = []
star = []

with open("star.json", "r", encoding="utf-8") as f:
    res = json.load(f)
    print(len(res["items"]), type(res["items"]))
    for item in res["items"]:
        name.append(item["name"])
        star.append(item["stargazers_count"])

plt.bar(name, star)
plt.xticks(rotation=45)
plt.show()