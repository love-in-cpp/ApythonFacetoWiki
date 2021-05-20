# -*- coding = utf-8 -*-
# @Time : 2021/4/30 19:12
# @Author : 刘正阳
# @File : spider.py
# @Software : PyCharm
import urllib.request
import re

import xlwt
from bs4 import BeautifulSoup

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)

    savepath = "豆瓣电影Top250.xls"
    # 3.保存数据
    saveData(datalist,savepath)
#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')#创建正则表示对象，()表示组，.*表示一个或多个字符
#影片的图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)#re.S表示忽略换行的情况，把/n也算在里面，即希望字符串是完整的不经过解释的字符串
#影片的片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
#影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

def getData(baseurl):
    datalist = []

    for i in range(0,10): #0-9,左闭右开
        url=baseurl+str(i*25)
        html = askURL(url)#保存获取到的网页源码
        # 2.逐一分析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串形成列表,组合属性查找div的class_=item
            # print(item)#打印item及其子目录#查看电影item的全部信息
            data = []  # 保存一部电影的所有信息
            item = str(item)  # 将一部电影的所有信息字符串化，接下来就可以用正则表达式对信息进行解析了
            # print(item)

            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串，需要给一个规则,#[0]表示这两个里面的第一个，因为返回的是列表
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名，没有外国名
            if (len(titles)) == 2:
                ctitle = titles[0]
                data.append(ctitle)

                otitle = titles[1].replace('/', '')  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')  # 留空，不能因为内容没有就不填，不然表就会很难看，外文名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评价人数

            inq = re.findall(findInq, item)  # 概述(bd)可能没有
            if len(inq) != 0:
                inq = inq[0].replace('。', '')  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', ' ', bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后空格

            datalist.append(data)
    # for item in datalist:
    #     print(item)
    return datalist


#得到指定一个URL的网页内容
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

def saveData(datalist,savepath):
    print("save...")
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook 对象

    worksheet = workbook.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表

    col = ('电影详情链接','图片链接','影片中文名','影片外文名','评分','评价数','概况','相关信息')
    for i in range(0, 8):
        worksheet.write(0,i,col[i])#写一行列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])#数据

    workbook.save(savepath)




if __name__ == "__main__":
    main()
    print('爬取完毕！')
    print('晚安')