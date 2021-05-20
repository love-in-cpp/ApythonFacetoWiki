# -*- coding = utf-8 -*-
# @Time : 2021/5/1 15:11
# @Author : 刘正阳
# @File : testBs4.py
# @Software : PyCharm

'''
BS4将html文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种：
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''
import re

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")#rb表示以二进制方式读取
html = file.read().decode("utf-8")#read()方法一次性读取文件全部内容
bs = BeautifulSoup(html,"html.parser")#传入一个文件，用html解析器解析，形成了文件树形结构

#1.Tag 标签及其内容，拿到它所找到的第一个内容   ↑👆
# print(bs.title)
# print(bs.a)
# print(bs.div)
# print(type(bs.head))#打印第一个head标签的所有内容


#2.NavigableString 标签里的内容 （字符串） ↑👆
# print(bs.title.string)
# print(type(bs.title.string))

#键值对存储的依据
#print(type(bs.a.attrs))

#3.BeautifulSoup 表示整个文档
#print(type(bs))
# print(bs.name)
# print(bs)

#4.Comment是一个特殊的NavigableString，输出的内容不包含注释符号 !--新闻 --
# print(bs.a.string)
#print(type(bs.a.string))


#----------------------------
#文档的遍历
# print(bs.head.contents)#获取Tag head 所有的子节点 返回一个 list
# print(bs.head.contents[1])#contents列表的第一个content

#更多内容，搜索BeautifulSoup文档

#文档的搜索
#(1) find_all(),查找所有a标签【超链接】，返回一个列表
#字符串过滤：会查找与字符串完全匹配的内容，必须完全一样
# t_list = bs.find_all("a")

#正则表达式搜索：使用search()方法来匹配内容
#只要标签含有a，就把标签里所有子内容全部找出来
# t_list= bs.find_all(re.compile("a"))#re.compile("a")表示编译一个正则表达式对象，然后去搜索符合正则表达式规则的内容

#方法 ： 传入一个函数（方法），根据函数的要求来检索（了解）
# def name_is_exists(tag):
#     return tag.has_attr("name")
#找出标签里有name标签的标签
# t_list=bs.find_all(name_is_exists)
# print(t_list)

#2.kwargs  参数
# t_list = bs.find_all(id="head")
#
# t_list = bs.find_all(class_=True)#class是python中关键字，需要加 _ 下划线区分
# t_list = bs.find_all(href="http://news.baidu.com")
#打印一个list对象
# for item in t_list:
#     print(item)

#3.text 参数

t_list = bs.find_all(text = "hao123")
t_list = bs.find_all(text = ["hao123","地图","贴吧"])
t_list = bs.find_all(text = re.compile("\d"))#应用正则表达式来查找包含特定文本的内容（标签里的字符串），并不是完整的标签

#4.limit 参数,限制结果的数量

t_list = bs.find_all("a",limit=3)

#css选择器
t_list = bs.select('title')#通过标签来查找

t_list = bs.select(".mnav")#通过类名来查找css用 . 来表示class=mnav 通过类名查找 ,# t_list = bs.find_all(class_="mnav")

t_list = bs.select("#u1") #通过id查找，css用#表示id

t_list = bs.select("a[class='bri']") #通过属性来查找，找出a标签里的class = bri属性，返回整个标签

t_list = bs.select("head>title") #通过子标签来查找

t_list = bs.select(".mnav ~ .bri")#跟mnav是兄弟的标签，而且标签内容是bri

print(t_list[0].get_text())#得到文本

for item in t_list:
    print(item)



