##encoding=utf8

'''
https://www.rxpricequotes.com/
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
#     for i in 'abcedfghijklmnopqrstuvwxyz ':
#         for j in 'abcedfghijklmnopqrstuvwxyz ':
            query_list.append(i+j)
    return query_list

def enter_query(text, t = 0.1):
    '''
    1.清空错误信息
    2.定位到搜索框
    3.清空搜索框
    4.输入关键字
    '''
    Double_click(632, 205, dl=t) # 错误文本框 全屏1087, 168 小窗610, 186
    Double_click(347, 314, dl=t) # 搜索文本框 全屏802, 322 小窗303, 339
    Ctrl_a(dl=t)
    Delete(dl=t)
    Type_String(text, dl=t)

def main():
    try:
        druglist = set(load_jt('druglist.json'))
    except:
        druglist = set()  
    query_list = generate_querylist()
    
    Delay(1)
    drugname = ''
    for query in query_list:
        for i in range(1,51):
            print 'Now crawling %s - %s' % (query, i)
            Delay(0.5)
            enter_query(query, t = 0.1)
            Delay(4)
            Down(i, dl=0.1)
            Enter(dl=0.5)
            Ctrl_a(dl=0.5)
            Ctrl_c(dl=0.5)
            try:
                if pyperclip.paste() == drugname: # 如过跟上一次重复，就跳过
                    break
                else:
                    drugname = pyperclip.paste()
                    druglist.add(drugname)
                    dump_jt(list(druglist), 'druglist.json', replace = True)
            except:
                pass
# print WhereXY()
Delay(10)
main()