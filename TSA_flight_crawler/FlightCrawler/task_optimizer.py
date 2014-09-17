##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-12

from HSH.Data.jt import *
from datetime import datetime, timedelta
from collections import OrderedDict
import jsontree
import os
# fname_dpt = r'reference/tsk_opt_dpt.json'
# fname_arv = r'reference/tsk_opt_arv.json'
# 
# tsk_opt_dpt = load_jt(fname_dpt)
# tsk_opt_arv = load_jt(fname_arv)
'''
tsk_opt = {date1 : {airport1 : counter,
                    airport2 : counter, ...}
           date2 : {samething} }
'''

class Task_optimizer(object):
    '''对于每天的机场数据，爬虫永远优先爬那些没有被爬过的机场
    '''
    def __init__(self, fname):
        if os.path.exists(fname): # exists, then load
            with open(fname, 'rb') as f:
                self.data = jsontree.loads(f.read())
        else:
            print '%s not exists! cannot load!, initialing task optimizer...' % fname
            airport_codelist = ["ORD", "DFW", "CLT", "IAH", "SFO", "PHL", "EWR", "BOS", "PHX", "LAS", "SLC", "SAN", "STL", "MDW", "PDX", "BNA", "IND", "CVG", "AUS", "ANC", "MSY", "SJC", "JAX", "MKE", "MEM", "SDF", "HOU", "BDL", "OKC", "ABQ", "SYR", "GSO", "SJU", "TUL", "GRR", "ROC", "ELP", "RNO", "SAV", "OGG", "BOI", "LIH", "LEX", "PVD", "ALB", "HSV", "MDT", "CID", "CAE", "BTR", "MHT", "XNA", "FAI", "MAF", "CAK", "SBA", "MLI", "MOB", "ACK", "SGF", "SHV", "PIA", "GPT", "CHO", "AMA", "FAR", "BIL", "CRW", "BET", "FNT", "PWM", "AVL", "PHF", "SBN", "ATW", "MGM", "GNV", "MSO", "RDM", "BZN", "BMI", "LRD", "ABI", "HYA", "FAY", "BLI", "BIS", "SCE", "AVP", "MLU", "KTN", "CWA", "CMI", "HRL", "CLL", "TRI", "DLH", "OAJ", "RST", "PIR", "ISN", "IDA", "FSM", "OTZ", "MOT", "BFL", "SWF", "SPS", "YUM", "ERI", "LCH", "ROW", "OME", "MQT", "DBQ", "DUT", "YKM", "FLG", "SPI", "SMX", "UIN", "MKK", "LAW", "OTH", "VDZ", "SUN", "EAR", "ALS", "PRC", "PLN", "SCC", "FLO", "PQI", "GRI", "PDT", "COU", "RDD", "SIT", "GGG", "HRO", "HVN", "SLN", "ILI", "MTJ", "LWS", "HON", "PGA", "RHI", "SUX", "PVC", "RUT", "HPB", "BQK", "TAL", "SHR", "VLD", "ALW", "CEZ", "ATY", "BPT", "JLN", "TVF", "OWB", "ELD", "CIC", "RKS", "EKO", "LMT", "APN", "PKA", "BTT", "BTI", "WNA", "CDB", "JHM", "GST", "BRD", "ESC", "KKI", "GNU", "TOG", "AOO", "PKB", "MGW", "DUJ", "YAK", "TUP", "KWT", "MCN", "PAH", "PSM", "CVO", "AIA", "SVA", "PTU", "TEX", "TWF", "WRG", "GLV", "VEL", "WTK", "KSM", "JBR", "KWN", "HSL", "DRG", "MOD", "HNS", "MKG", "WMO", "EEK", "ELI", "MSS", "UTO", "CBE", "INL", "FNL", "EEN", "EMK", "UCA", "SLE", "PIP", "ATK", "KTB", "MEI", "TOL", "AGN", "HYL", "KNW", "EDA", "PIB", "IGG", "JGC", "GCN", "KGK", "NIB", "HII", "KAE", "DTT", "AKB", "CNY", "WST", "ANV", "QWF", "HUF", "SLQ", "BLF", "KVC", "SHH", "KWK", "RSJ", "MLL", "WKK", "PPV", "KKH", "ORV", "CLP", "DJN", "CVN", "LWT", "LAR", "SKK", "PLB", "ADK", "KMO", "SHX", "TSM", "KCL", "BWG", "JVL", "PQS", "WBQ", "ABL", "SHG", "WMK", "WDG", "KPB", "TEH", "ILE", "ELV", "GLH", "KAL", "RSH", "PEC", "WBU", "MCW", "KPC", "XHH", "QKS", "HKY", "TWA", "WLK", "MLY", "IFP", "WSX", "CNM", "TCL", "PNC", "CGX", "KKU", "ORT", "NKI", "SDL", "POU", "YNG", "KUK", "HCR", "ZBV", "MKT", "CEM", "LPS", "RBY", "CHP", "WMH", "OXR", "SBS", "AIY", "MBL", "EAU", "RMP", "HVR", "KLW", "RDV", "QCE", "TKJ", "CUW", "HUS", "SOP", "ORL", "SVC", "CGA", "LUP", "VEE", "OSH", "WBB", "MOU", "GYY", "MWH", "PAK"]
            self.data = {dt : { airport_code : 0 for airport_code in airport_codelist} for dt in dt_interval_generator('2014-09-10', '2014-12-30')}
        self.path = fname
        
    def _dump(self):
        dump_jt(self.data, self.path, fastmode = True, replace = True)
        
    def add(self, date, airport_code):
        try:
            self.data[date][airport_code] += 1
        except:
            print 'failed to add value in date = %s, airpot = %s' % (date, airport_code)
            
    def next_airport(self, date):
        od = OrderedDict( sorted(self.data[date].items(), 
                             key=lambda t: t[1], ## t[0]指根据key排序, t[1]指根据value排序
                             reverse = False) ) ## True指逆序排序，False指正序排序
        for airport_code in od.iterkeys():
            break
        return airport_code
        
    def opt_list(self, date):
        od = OrderedDict( sorted(self.data[date].items(), 
                             key=lambda t: t[1], ## t[0]指根据key排序, t[1]指根据value排序
                             reverse = False) ) ## True指逆序排序，False指正序排序
        return list( od.iterkeys() )
         
def dt_interval_generator(start, end):
    ''' 
    INPUT = ('2014-01-01', '2014-01-03')
    yield 2014-01-01, 2014-01-02, 2014-01-03
    '''
    start, end = datetime.strptime(start, '%Y-%m-%d'), datetime.strptime(end, '%Y-%m-%d')
    delta = timedelta(1)
    for i in xrange( (end-start).days + 1):
        dt = start + i * delta
        yield datetime.strftime( dt, '%Y-%m-%d')
        
if __name__ == '__main__':
    topt = Task_optimizer('nice.json')
    topt.add('2014-09-10', 'DCA')
    for i in xrange(5):
        airport = topt.next_airport('2014-09-10')
        print airport
        topt.add('2014-09-10', airport)
    topt._dump()
#     dump_jt(topt.data, 'topt.json', fastmode = True, replace = True)
