##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-02

'''
Useful funcationality repack from geopy
'''
from geopy.geocoders import GoogleV3
from geopy.distance import vincenty
from LinearSpider.jt import *
import jsontree
import sys

def dist(coordinate1, coordinate2, unit = 'mile'):
    '''Calculate distance
    INPUT: coordinate tuple = (longitude, latitude) in decimal format (not degree)
    Output: distance in mileage, kilometers or feet. Default is mileage.
    '''
    distance = vincenty(coordinate1, coordinate2)
    if unit == 'mile':
        return distance.miles
    elif unit == 'km':
        return distance.kilometers
    elif unit == 'feet':
        return distance.feet
    else:
        print 'Error! please set unit as "mile", "km" or "feet".'
        return None

def batch_geocoding(list_of_addrs, fname):
    geodata = load_jt(fname)
    engine = GoogleV3('AIzaSyBq-NZmY8G6Tm7Fzpx4dAR55Uk0n-5AIDQ')
    print 'Warning! Calling Google Geocoding API'
    for addr in list_of_addrs:
        if addr not in geodata:
            location = engine.geocode(addr)
            LOC = location.raw
            print sys.getsizeof(LOC)

def unit_test1():
    cd1 = (38.953165, -77.396170) # EFA
    cd2 = (38.899697, -77.048557) # GWU
    print dist(cd1, cd2)

def unit_test2():
    list_of_addrs = ['1400 S Joyce St, VA, 22202', 'bgqwrj']
    batch_geocoding(list_of_addrs, 'geodata.json')
    
if __name__ == '__main__':
#     unit_test1()
    unit_test2()