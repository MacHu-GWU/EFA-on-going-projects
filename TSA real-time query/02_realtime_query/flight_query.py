##encoding=utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time
import sys

reload(sys); # change the system default encoding = utf-8
eval("sys.setdefaultencoding('utf-8')")

def sleep(n):
    time.sleep(n)
    print '\t wake up from %s second.' % n
    
def query(airport, date):
    driver = webdriver.Firefox()
    driver.get('http://www.flightstats.com/go/FlightStatus/flightStatusByFlight.do?')
    sleep(3)
    
    ## fill the form
    element = driver.find_element_by_id('byAirport') # click "byAirport" make airport box visible
    element.click()

    element = driver.find_element_by_id('fsByAirportDepartureDateTextField') # enter date
    element.clear()
    element.send_keys(date)
     
    element = driver.find_element_by_id('fsAirport') # enter airport code
    element.clear()
    element.send_keys(airport)
    
    element.send_keys(Keys.RETURN) # send request
    sleep(1)
    
    ## select different option
    select = Select(driver.find_element_by_xpath("//div[@class='uiComponent674']//select[@id='airportQueryTime']"))
    options = [element.text for element in select.options] # get time period options
    
    for option in options:
        sleep(1)
        select.select_by_visible_text(option)
        
query(airport = 'LAX', date = '2014-09-10')





