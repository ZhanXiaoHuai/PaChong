import requests

url='https://fanyi.baidu.com/ait/text/translate'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
}

#input_word=input('请输入要翻译的单词:')

data={
    'from':'en',
    'to':'zh',
    'query':'dog'
}

response=requests.post(url=url,headers=headers,data=data)

dic_obj=response.json()
print(dic_obj)