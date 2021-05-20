# -*- coding = utf-8 -*-
# @Time : 2021/5/9 15:10
# @Author : 刘正阳
# @File : spiderfc.py
# @Software : PyCharm

import urllib.request
import re
import xlwt
from bs4 import BeautifulSoup


def main():

    baseurl = 'https://zh.wikipedia.org/wiki/Category:%E4%B8%AD%E5%9B%BD%E7%94%9F%E7%89%A9%E5%AD%A6%E5%AE%B6'
    print('write...')
    datalist = getData(baseurl)
    print('done')
    savepath = "中国生物学家.xls"
    # 3.保存数据
    saveData(datalist, savepath)
    print('中国生物学家信息已爬取完毕！')

def askURL(url):
    head={
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 89.0.4389.72Safari / 537.36"
    }#本质上是告诉浏览器，我们可以接收什么样的文件内容
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)#响应传入的是请求信息
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if(hasattr(e,"code")):
            print(e.code)
        if(hasattr(e,"reason")):
            print(e.reason)
    return html

def getData(baseurl):

    datalist = []

    html = askURL(baseurl)  # 保存获取到的网页源码

    url_s = []#父网页想要提取的href
    # 2.逐一分析数据
    soup_html = BeautifulSoup(html, "html.parser")#父网页的html文档
    target_div = soup_html.find(id="mw-pages")
    li = target_div.find_all('li')
    li_c = li[1:-1]
    findUrl = re.compile(r'<li><a href="(.*?)" title=')
    findBirth = re.compile(r'</b>(\s*)（(.*?)年')
    url = []
    for item in li_c:
        temp = re.findall(findUrl, str(item))
        url.append(temp)

    for item in url:
        url_s.append('https://zh.wikipedia.org'+item[0])

    count = 0
    for item in url_s:
        html_s = askURL(item)  # 一个科学家的html文档
        soup_s = BeautifulSoup(html_s, "html.parser")
        content_div = soup_s.find(class_='mw-parser-output')  # 简介和生平
        p = content_div.find_all('p')  # p[0]简介，p[1]生平
        name = p[0].find('b')  # 名字
        s = str(p[0])
        try:
            birth = re.findall(findBirth,s)[0][1]#出生年份
        except IndexError as e:
            birth = None
        print(birth)
        if(len(p)>=2):
            data = []
            if name is None:
                data.append('null')
            else:
                data.append(name.text)
            if p[0] is None:
                data.append('null')
            else:
                data.append(p[0].text)
            if p[1] is None:
                data.append('null')
            else:
                data.append(p[1].text)
            if birth is None :
                data.append('null')
            elif len(birth)>5:
                data.append('null')
            else:
                data.append(birth)
        elif (len(p) == 1):
            data = []
            if name is None:
                data.append('null')
            else:
                data.append(name.text)
            if p[0] is None:
                data.append('null')
            else:
                data.append(p[0].text)
            data.append('null')
            if birth is None:
                data.append('null')
            else:
                data.append(birth)
        else:
            data = []
            data.append('null')
            data.append('null')
            data.append('null')
        count += 1

        print("正在向内存写入第%d条" % (count))
        datalist.append(data)
    #     if(count>=10):
    #         break
    # for item in datalist:
    #     print(item)
    print(len(datalist))
    return datalist

def saveData(datalist,savepath):
    print("save...")
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook 对象

    worksheet = workbook.add_sheet('中国生物学家',cell_overwrite_ok=True)  # 创建工作表

    col = ('姓名','简介','生平','出生年份')
    for i in range(0, 4):
        worksheet.write(0,i,col[i])#写一行列名
    for i in range(0,68):
        print("正在向外存写入第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,4):
            worksheet.write(i+1,j,data[j])#数据

    workbook.save(savepath)

if __name__ == "__main__":
    main()






