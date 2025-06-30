import requests
import json

#Ajax数据 豆瓣电影-排行榜-喜剧
url='https://movie.douban.com/j/chart/top_list'

#get的参数就是params post的参数就是data
param={
    'type':'24',
    'interval_id':'100:90',
    'action':'',
    'start':'0',#从库中的第几部电影 经过取出来之后从0开始计算
    'limit':'20'#一次取出的个数
}

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
}

response=requests.get(url=url,params=param,headers=headers)
list_data=response.json()#返回一个列表
print(list_data)
#持久化存储
fp=open('./douban.json','w',encoding='utf-8')

json.dump(list_data,fp=fp,ensure_ascii=False)#写入什么数据，写到哪去，防止乱码

print('over!!!')
