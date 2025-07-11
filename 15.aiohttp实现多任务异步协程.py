import requests
import asyncio
import time

from Tools.scripts.verify_ensurepip_wheels import print_notice

start=time.time()

urls=[
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]

async def get_page(url):
    print('正在下载',url)
    response=requests.get(url=url)#requests.get基于同步模块的代码 所以无法实现异步操作
    #aiohttp:基于异步网络请求的模块
    print('下载完毕： ',response.text)

tasks=[]

for url in urls:
    c=get_page(url)#返回协程对象
    task=asyncio.ensure_future(c)#协程对象封装到任务对象中
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))#多任务注册到循环事件中

end=time.time()
print('总耗时:',end-start)