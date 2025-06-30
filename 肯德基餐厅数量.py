import json

import requests
from fake_useragent import UserAgent
#Ajax数据 KFC 餐厅查询
url='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

data={
    'cname':'深圳',
    'pid':'',
    'keyword':'西丽',
    'pageIndex':'1',
    'pageSize':'20'
}

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
}


response=requests.post(url=url,data=data,headers=headers)

list_data=response.text

print(list_data)
fp=open('./KFC.json','w',encoding='utf-8')
json.dump(list_data,fp,ensure_ascii=False)
#fp.write(list_data)