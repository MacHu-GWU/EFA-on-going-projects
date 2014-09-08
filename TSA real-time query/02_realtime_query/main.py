##encoding=utf8
import selenium
import time
import sys
from LinearSpider.crawler import Crawler
from LinearSpider.jt import load_jt, dump_jt, prt_jt, d2j, ignore_iterkeys, ignore_itervalues, ignore_iteritems
from bs4 import BeautifulSoup as BS4

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")')

def sleep(n):
    time.sleep(n)
    print '\t wake up from %s second.' % n
    
def unit_test1():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Firefox()
    driver.get("http://www.flightstats.com/go/FlightStatus/flightStatusByFlight.do?")
    sleep(6)
    element = driver.find_element_by_id("byAirport")
    element.click()
    element = driver.find_element_by_id("fsAirport")
    element.clear()
    element.send_keys("LAX")
    element.send_keys(Keys.RETURN)    

#     html = driver.page_source
#     with open('test.html', 'wb') as f:
#         f.write(html)
#     driver.close()

# unit_test1()

def unit_test2():
    url = 'http://www.flightstats.com/go/FlightStatus/flightStatusByAirport.do;jsessionid=7B477D6D5CFB639F96C5D855CEB941D0.web4:8009?airport=LAX&airportQueryDate=2014-09-06&airportQueryTime=-1&airlineToFilter=&airportQueryType=0&x=0&y=0'
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(6)
    
#     element = driver.find_element_by_id("airportQueryTime")[1]
#     element.click()
    
    sleep(2)
    element = driver.find_element_by_xpath("//select[@id='airportQueryTime']/option[@value='0']")
    element.click()
    
unit_test2()
if __name__ == '__main__':
    
    pass

