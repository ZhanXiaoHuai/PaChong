import asyncio

async def request(url):
    print('正在执行的url为',url)
    print('请求成功',url)
    return url
#async修饰的函数，调用完之后返回一个携程对象
c=request('www.baidu.com')

# #创建一个事件循环对象
# loop=asyncio.get_event_loop()
#
# loop.run_until_complete(c)


# #task的使用 需要基于事件循环 .出create_task 其他和future没区别
# loop=asyncio.get_event_loop()
# #基于loop创建了一个task对象
# task=loop.create_task(c)
# print(task)#pending状态
# loop.run_until_complete(task)
# print(task)#finished状态

# #future的使用 和task结果一样 都是任务对象
# loop=asyncio.get_event_loop()
# task=asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

#绑定回调

def callback_func(task):
    #result返回的就是任务对象中封装的携程对象对应函数的返回值
    print(task.result())#’www.baidu.com‘

loop=asyncio.get_event_loop()
task=asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)

loop.run_until_complete(task)


