# -*- coding = utf-8 -*-
# @Time : 2021/5/15 17:36
# @Author : 刘正阳
# @File : t.py
# @Software : PyCharm
def trim(s):

    front_index = 0
    for i in range(0, len(s)):
        if s[i] != ' ':
            front_index = i
            break

    after_index = 0
    s_i = s[::-1]
    for i in range(0, len(s)):
        if s_i[i] != ' ':
            after_index = len(s) - i
            break

    s = s[front_index:after_index]
    return s
