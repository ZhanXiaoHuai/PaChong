#使用该模块中ClientSession
import requests
import asyncio
import time
import aiohttp

from Tools.scripts.verify_ensurepip_wheels import print_notice

start=time.time()

urls=[
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]

async def get_page(url):
    #aiohttp:基于异步网络请求的模块
    async with aiohttp.ClientSession() as session:
        #get()、post():
        #headers=... ,params/data,proxy='http://ip:port' 除了代理IP不一样 其他是一样的 代理的名字不一样 而且传的是字符串
        async with await session.get(url) as response:#所有的with前面都要用async修饰  get是阻塞的 用await进行挂起
            #text()返回字符串形式的响应数据
            #read()返回的二进制形式的响应数据
            #json()返回的说就是json对象
            #和requests模块调用的还是有区别
            page_text=await response.text()#注意： 在获取响应数据操作之前一定要用await进行手动挂起 不然拿不到数据
            print(page_text)

tasks=[]

for url in urls:
    c=get_page(url)#返回协程对象
    task=asyncio.ensure_future(c)#协程对象封装到任务对象中
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))#多任务注册到循环事件中

end=time.time()
print('总耗时:',end-start)