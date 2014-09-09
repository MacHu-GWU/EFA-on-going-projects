from LinearSpider.jt import *

# print len(load_jt(r'backup\address_geocoded.json'))
print len(set(load_jt(r'address_geocoded.json').keys()))
print len(set(load_jt(r'address_list.json')))

def googleV3_json_example():
    geo = load_jt(r'backup\address_geocoded_example.json')
    for raw_addr, v in geo.iteritems():
        print v['address_components'][0]['long_name'] # street number
        print v['address_components'][1]['long_name'] # route
        print v['address_components'][2]['long_name'] # neighborhood
        print v['address_components'][3]['long_name'] # locality - local name
        print v['address_components'][4]['long_name'] # city - county name
        print v['address_components'][5]['long_name'] # state
        print v['address_components'][6]['long_name'] # country
        print v['address_components'][7]['long_name'] # postal_code
        print v['formatted_address'] # = street number + route, locality, state + postal_code, country
        print v['geometry']['location']['lat'] # coordinate1
        print v['geometry']['location']['lng'] # coordinate2
        
if __name__ == '__main__':
    googleV3_json_example()