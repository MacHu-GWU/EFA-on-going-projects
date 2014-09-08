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

def row_generator(tag_tr):
    def process_space(text):
        text = text.strip()
        text = text.replace('\n', '')
        text = text.replace('\r', '')
        return text
#     print tag_tr.prettify()
    results = tag_tr.find_all('td')
    row = (process_space(results[0].text),
           process_space(results[1].text),
           process_space(results[2].text),
           process_space(results[3].text),
           process_space(results[4].text),
           process_space(results[5].text),
           process_space(results[6].text),
           process_space(results[7].text),
           process_space(results[8].text),
           process_space(results[9].text))
    return row
    
with open('example2.html', 'rb') as f:
    html = f.read()
    
soup = BS4(html)
c = itertools.count()
for tr in soup.find_all('tr', attrs = {}):
    try:
        print row_generator(tr), c.next()
    except:
        pass
    
# 注意 u'Landed\xa0 On-time' 对应着一些延迟的标志
