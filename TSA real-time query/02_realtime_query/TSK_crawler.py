##encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from LinearSpider.crawler import Crawler
from LinearSpider.jt import load_jt, dump_jt, prt_jt, d2j, ignore_iterkeys, ignore_itervalues, ignore_iteritems
from bs4 import BeautifulSoup as BS4

import datetime
import time
import sys
import os

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")')
os.chdir(r'C:\HSH\Workspace\py27_projects\EFA-on-going-projects\TSA real-time query\data')

def sleep(n):
    time.sleep(n)
    print '\t wake up from %s second.' % n
    
def locate_source(date, airport_code):
    driver = webdriver.Firefox()
    driver.get(entrance_url)
    sleep(6)
    
    element = driver.find_element_by_id("byAirport") # 选中 byairport
    element.click()

    element = driver.find_element_by_id("fsByAirportDepartureDateTextField") # 在 date 内输入时间
    element.clear()
    element.send_keys("2014-09-11")

    element = driver.find_element_by_id("fsAirport") # 在 airport 内输入文本
    element.clear()
    element.send_keys("LAX")
    
    element.send_keys(Keys.RETURN) # 提交文本
    
    select = Select(driver.find_element_by_xpath("//div[@class='uiComponent674']//select[@id='airportQueryTime']"))
    options = [element.text for element in select.options]
    print options
    for option in options:
        select.select_by_visible_text('6:00AM - 7:00AM')
        
#     sleep(6)
#     driver.close()
entrance_url = 'http://www.flightstats.com/go/FlightStatus/flightStatusByFlight.do?'
# locate_source(date = "2014-09-10", airport_code = "LAX")

text = '6:00AM - 7:00AM'
def pro_text(text):
    st, et = text.split('-')
    st, et = st.strip(), et.strip()
    st, et = time.strptime(st, '%I:00%p').tm_hour, time.strptime(et, '%I:00%p').tm_hour
    return '%s-%s' % (st, et)
print pro_text(text)
