# -*- coding = utf-8 -*-
# @Time : 2021/4/30 19:13
# @Author : 刘正阳
# @File : testable1.py
# @Software : PyCharm

import urllib.request
# #获得一个get请求,超时处理需要有计划性的请求
# #防止没响应就设置timeout（最长等待时间），为了让程序出异常还接着运行，try except机制
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode('utf-8'))#对获取网页的源码进行utf-8解码
# except urllib.error.URLError as e:#别名e
#     print("time out")

#获得一个post请求
#模拟用户真实登录时用post请求
'''
post请求是什么？
为什么要传递post的表单信息？

#urlopen的作用是把一个字典转换成字符串，bytes()的作用是把这个字符串再转成二进制格式，因为post方式需要的参数是二进制的

通过表单信息的封装才能正常访问post
像提交表单请求一样，分配一个data。
bytes()转二进制
parse（解析器）把键值对按utf-8的格式解析，统一变成二进制，封装成byte数组，形成data
'''
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#print(response.status)#状态码200表示正常响应，418表示我是一个茶壶，爬虫被发现
#print(response.getheaders("Server")) #返回的是列表list,引号内可以指出要访问的具体数值

# url="http://www.douban.com"
# url="http://httpbin.org/post"
#伪装
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
# }
# data=bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")#必须大写POST，否则http400
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

#实际上不需要这么多信息，只需要伪装headers
url="https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}
req= urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))