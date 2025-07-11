import time
import asyncio

async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步.
    #time.sleep(2)
    #当在asyncio中遇到阻塞操作必须进行手动挂起 await
    await asyncio.sleep(2)#基于异步的 用这个
    print('下载完成', url)


start_time=time.time()

urls=[
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia/com'
]

#任务列表 存放多个任务对象
stacks=[]
for url in urls:
    c=request(url)#返回一个协程对象
    task=asyncio.ensure_future(c)
    stacks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stacks))#不能直接将列表传进来 要经过wait封装 不然就是最开始的task直接传进来

print(time.time()-start_time)#看执行了多久 异步