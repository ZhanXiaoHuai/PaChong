from lxml import etree



if __name__=='__main__':
    #示例好了一个etree对象，且被解析的源码加载到了该对象中
    tree=etree.parse('HTML表单.html',etree.HTMLParser())#本地存储用parse 网络上的用比如HTML()
    #r=tree.xpath('/html/body/form/div')#一个/代表一个层级 开头加/表示根节点
    #r=tree.xpath('/html/body//div')#//略过一个层级 结果一样和上面
    #r = tree.xpath('//div')  # //作用到最左侧 表示寻找任意的位置的div 找到所有的 结果一样和上面
    #r=tree.xpath('//div[@class="hero_adc"]')#属性定位 class=这个的div xpath返回的都是一个列表
    #r = tree.xpath('//div[@class="hero_adc_2"]/p[1]')  # 索引定位 从1开始计数 没有0

    #r=tree.xpath('//div[@class="hero_adc_2"]//li[2]/a/text()')[0]#text()取得标签的文本 但是返回的是列表类型 所以在外面取[0] 获得文本
    #r = tree.xpath('//li[2]//text()')[0]#获取非直系的文本 标签里面标签的文本//text()
    #r=tree.xpath('//div[@class="hero_adc_2"]//text()')#///text示例 定位到div=hero_adc_2下所有的文本
    r=tree.xpath('//div[@class="hero_adc_2"]/img/@src')#取属性值 /@attName /src 要什么就取什么

    print(r)
