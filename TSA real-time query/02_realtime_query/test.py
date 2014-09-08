## my question post on stack overflow
## http://stackoverflow.com/questions/25706799/interact-with-an-invisible-element-and-access-second-matching-element

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


url = 'http://www.flightstats.com/go/FlightStatus/flightStatusByAirport.do;jsessionid=7B477D6D5CFB639F96C5D855CEB941D0.web4:8009?airport=LAX&airportQueryDate=2014-09-06&airportQueryTime=-1&airlineToFilter=&airportQueryType=0&x=0&y=0'
driver = webdriver.Firefox()
driver.get(url)

select = Select(driver.find_element_by_xpath("//div[@class='uiComponent674']//select[@id='airportQueryTime']"))

# print all the options
print [element.text for element in select.options]

# select option by text
select.select_by_visible_text('6:00AM - 7:00AM')