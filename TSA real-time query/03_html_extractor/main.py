##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-06

'''
Crawl airport code
source = http://www.airportcodes.org/
'''

from LinearSpider.jt import load_jt, dump_jt, prt_jt, d2j, ignore_iterkeys, ignore_itervalues, ignore_iteritems
from bs4 import BeautifulSoup as BS4
import itertools

def row_generator(tag_tr, valid_airport_code):
    '''extract destination, flight, airline, scheduled_time, actual_time, Terminal_Gate, status, equip
    from one row html element
    '''
    def process_space(text):
        '''handle unexpected \n \r
        '''
        text = text.strip()
        text = text.replace('\n', '')
        text = text.replace('\r', '')
        return text
    
    def replace_special_char(text):
        '''delete unexpected char
        \xa0, \a0124, etc indicate delayed severity
        "^" indicate it's a code share flight
        "~" indicate it's a estimated time
        '''
        special_char1 = [u'\xa0', u'\xa0124', u'\xa031', u'\xa028']
        special_char2 = [u'^', u'~']
        for char in special_char1:
            text = text.replace(char, ' ')
        for char in special_char2:
            text = text.replace(char, '')
        return text
    
    results = tag_tr.find_all('td') # 每个td是一个列元素
    destination = process_space(results[0].text)
    flight = replace_special_char( process_space(results[1].text) )
#     on_time_rating = process_space(results[2].text)
    airline = process_space(results[3].text)
    scheduled_time = process_space(results[4].text)
    actual_time = replace_special_char( process_space(results[5].text) )
    Terminal_Gate = process_space(results[6].text)
    status = replace_special_char( process_space(results[7].text) )
    equip = process_space(results[8].text)
#     track = process_space(results[9].text)
    return destination, flight, airline, scheduled_time, actual_time, Terminal_Gate, status, equip

def records_generator_from_html(html):
    '''从html中生成：
    目的地，航班号，航空公司，预计到达时间，实际到达时间，航站楼登记门，准时状态，飞机型号
    '''
    soup = BS4(html)
    c = itertools.count()
    
    for tr in soup.find_all('tr', attrs = {}):
        try:
            destination, flight, airline, scheduled_time, actual_time, Terminal_Gate, status, equip = row_generator(tr, valid_airport_code)
            if c.next() >= 2: # 从第3个tr tag开始，才是正确的航班信息
                yield destination, flight, airline, scheduled_time, actual_time, Terminal_Gate, status, equip
        except:
            pass

with open('example.html', 'rb') as f:
    html = f.read()
valid_airport_code = load_jt('US_airport_code.json').keys()

for record in records_generator_from_html(html):
    print record

