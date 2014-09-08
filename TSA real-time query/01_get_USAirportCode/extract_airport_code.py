##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-06

'''
Crawl airport code
source = http://www.airportcodes.org/
'''

from LinearSpider.jt import load_jt, dump_jt, prt_jt, d2j, ignore_iterkeys, ignore_itervalues, ignore_iteritems
import re

def strip_state(line):
    '''
    extract state from string like this:
        "#airport_name, #state_name (#airport_code)"
    for example:
        "Akiachak, AK (KKI)"
    '''
    state = line.split(',')[1]
    state = state.split('(')[0]
    return state.strip()

def extract_state_list():
    '''
    extract all US state short version (2 letters) from airport_code.json
    '''
    results = load_jt('airport_code.json')
    state_list = set()
    for result in results:
        try:
            state = strip_state(result)
            if len(state) == 2:
                state_list.add(state)
        except:
            pass
    dump_jt(list(state_list), 'state_list.json', replace = True)

def ETL_US_airport_code():
    '''extract #airport_code, #state, #airport_name
    '''
    results = load_jt('airport_code.json')
    state_list = load_jt('state_list.json')
    p_AirportCode = re.compile(r'(?<=\()[\s\S]{3}(?=\))') # Airport code Regex pattern
    US_airport_code = dict()
    
    for result in results:
        code = re.findall(p_AirportCode, result)[0] # extract airport code
        
        for state in state_list: # extract state
            if state in result: # if valid state in strings
                break
        
        info = result.replace('(%s)' % code, '').strip() # get airport name info
        
        US_airport_code.setdefault(code, {'state': state, # write to json data
                                          'airport_name': info})
    
    dump_jt(US_airport_code, 'US_airport_code.json', replace = True) # dump to local

if __name__ == '__main__':
    extract_state_list()
    ETL_US_airport_code()