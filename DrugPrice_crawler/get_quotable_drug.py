##encoding=utf8

'''python按键精灵脚本爬虫
目标 = https://www.rxpricequotes.com/
爬下这个网站数据库中所有的药品名称，这样我们就可以一个个的发送查询
然后爬下这个网站数据库中的所有价格信息
'''

import pyperclip
from HSH.RobotHand.macro import *
from HSH.Data.jt import *
import sys

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")')

def generate_querylist():
    query_list = list()
    for i in 'abcedfghijklmnopqrstuvwxyz ':
        for j in 'abcedfghijklmnopqrstuvwxyz ':
            query_list.append(i+j)
    return query_list

def enter_query(text, t = 0.1):
    '''
    1.清空错误信息
    2.定位到搜索框
    3.清空搜索框
    4.输入关键字
    '''
    double_click(610, 186, dl=t) # 错误文本框 1087, 168
    double_click(303, 339, dl=t) # 搜索文本框 802, 322
    Ctrl_a(dl=t)
    Delete(dl=t)
    type_string(text, dl=t)

def main():
    try:
        druglist = set(load_jt('druglist.json'))
    except:
        druglist = set()  
    query_list = generate_querylist()
    
    delay(1)
    for query in query_list:
        for i in range(1,51):
            enter_query(query, t = 0.1)
            delay(1)
            Down(i, dl=0.1)
            Enter(dl=0.1)
            Ctrl_a(dl=0.1)
            Ctrl_c(dl=0.1)
            druglist.add(pyperclip.paste())
            dump_jt(list(druglist), 'druglist.json', replace = True)
print whereXY()
# main()
