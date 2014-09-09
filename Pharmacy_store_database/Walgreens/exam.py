from LinearSpider.jt import *
from itertools import count


def exam1(): # 8190 store in total
    '''Find how many store walgreens has over US
    '''
    task = load_jt('walgreens_task.json')
    c = 0
    for entrance, v in ignore_iteritems(task):
        for state_url, v1 in ignore_iteritems(v):
            for city_url, v2 in ignore_iteritems(v1):
                for store_url, v3 in ignore_iteritems(v2):
                    c += 1
    print c
    
exam1()

def exam2(): # 8186, 4 stores link crashed
    '''Find how many store we have crawled
    '''
    walgreens = load_jt(r'walgreens_data.json')
    print len(walgreens)
    
exam2()