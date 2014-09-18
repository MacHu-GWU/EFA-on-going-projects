##encoding=utf8

from HSH.Data.jt import *

druglist = load_jt('druglist.json')

res = list()

for drug in druglist:
    if drug:
        if len(drug) > 2:
            if '\n' not in drug:
                res.append(drug)
        
dump_jt(res, 'clean_druglist.json', replace = True)