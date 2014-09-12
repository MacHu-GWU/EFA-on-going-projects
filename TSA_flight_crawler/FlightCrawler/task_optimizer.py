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
            airport_codelist = [u'AGN', u'SIT', u'WLK', u'YUM', u'SCC', u'NYC', u'CPR', u'AGS', u'OSH', u'SPS', u'SPI', u'BWD', u'BWG', u'TAL', u'BWI', u'KYU', u'VAK', u'ALO', u'WRL', u'EDA', u'EHM', u'DJN', u'LAN', u'JNU', u'SNA', u'PQI', u'LAF', u'AHN', u'PQS', u'LAX', u'SNP', u'MAF', u'LAW', u'LAR', u'LAS', u'GUC', u'BEH', u'TSM', u'CMI', u'CMH', u'ALB', u'SHR', u'BED', u'GUP', u'ISN', u'CMX', u'PCA', u'DTW', u'BET', u'DTT', u'HUF', u'LSE', u'KBC', u'AIN', u'VLD', u'SBA', u'TTN', u'HUS', u'CSG', u'HCR', u'GRR', u'KPV', u'BLV', u'IGG', u'KPB', u'DSM', u'BLI', u'ALW', u'IGM', u'BLF', u'KPN', u'GRI', u'CBE', u'KKU', u'INL', u'HLN', u'OKC', u'KKI', u'KKH', u'RIW', u'IND', u'GLH', u'SMX', u'AKP', u'AKI', u'SMK', u'AKN', u'AKB', u'GLV', u'MDJ', u'GGW', u'HYG', u'WHH', u'JST', u'LFT', u'GGG', u'MGW', u'MDW', u'MDT', u'AUG', u'JHM', u'AUK', u'AUS', u'VEE', u'VEL', u'WSN', u'SBS', u'SBP', u'ALM', u'ORV', u'ORT', u'SBY', u'LMT', u'PUB', u'ORL', u'MKT', u'ORH', u'ORF', u'LMA', u'ORD', u'PUW', u'SBN', u'ALS', u'WRG', u'KOA', u'UNK', u'XHH', u'CAK', u'TOL', u'RCE', u'ERI', u'CAE', u'IAH', u'VPS', u'PGA', u'QKB', u'KOT', u'PGV', u'HIB', u'IAD', u'QKS', u'KCQ', u'SVA', u'ONT', u'STG', u'ABE', u'STC', u'STL', u'ABI', u'HGR', u'KTS', u'ABQ', u'KTN', u'STS', u'ZRK', u'KTB', u'SMF', u'BHM', u'RSJ', u'PNS', u'BHB', u'OGS', u'CFA', u'TLT', u'NCN', u'RST', u'OGG', u'RSW', u'JFK', u'FNT', u'MIA', u'LIH', u'LIT', u'FNL', u'EGE', u'SAN', u'PRC', u'AOO', u'SAF', u'LBB', u'LBE', u'RAP', u'LBF', u'BYA', u'WTL', u'LBL', u'SAT', u'CHA', u'MRY', u'JAX', u'BFD', u'CHI', u'LPS', u'BFL', u'CHP', u'HRL', u'HRO', u'CHS', u'CHU', u'EYW', u'HII', u'JAC', u'KAE', u'QBF', u'IPL', u'KAL', u'RHI', u'SFO', u'APN', u'IPT', u'DBQ', u'APF', u'TYR', u'TYS', u'IFP', u'KSM', u'HDN', u'TKE', u'CEC', u'SYR', u'UGB', u'CEM', u'BMI', u'TKJ', u'PKB', u'PKA', u'NLG', u'SUX', u'CEZ', u'ENA', u'GCC', u'DLG', u'SHV', u'SHX', u'ABL', u'GCK', u'DLH', u'OXR', u'GCN', u'SHD', u'SHG', u'SHH', u'BTT', u'BTV', u'BTR', u'KXA', u'ABR', u'MGM', u'CZN', u'TBN', u'BTM', u'BTI', u'LUP', u'LUR', u'WYS', u'JBR', u'ATL', u'ISP', u'ATK', u'MUE', u'ATW', u'NUP', u'HYL', u'CRW', u'RMP', u'IRC', u'LNY', u'PVC', u'LNS', u'NUL', u'PVD', u'ASE', u'NUI', u'CLL', u'CLM', u'DUJ', u'LNK', u'GTF', u'PDX', u'CLD', u'CLE', u'EUG', u'PDT', u'GTR', u'IMT', u'YAK', u'CLT', u'RSH', u'TLH', u'DUT', u'PDB', u'ITO', u'OMA', u'KEK', u'ITH', u'HVN', u'TUP', u'TUS', u'TUL', u'HVR', u'CUW', u'WBU', u'WBQ', u'SWD', u'EKO', u'SWF', u'RDV', u'WBB', u'BPT', u'CYS', u'BIL', u'KWF', u'BID', u'ADQ', u'KWN', u'EUE', u'FYV', u'EVV', u'UCA', u'BIS', u'GYY', u'MLB', u'DHN', u'GON', u'FKL', u'RBY', u'MLI', u'SLQ', u'MLL', u'MLS', u'SLN', u'VCT', u'SJT', u'RBH', u'CWA', u'SLE', u'MLY', u'PNC', u'SLC', u'OTH', u'MCN', u'WKK', u'MCK', u'OTM', u'MCI', u'LGB', u'MCE', u'LGA', u'GFK', u'OTZ', u'MCW', u'CKB', u'CKO', u'BGM', u'BGR', u'SLK', u'PAH', u'PAK', u'CKX', u'IWD', u'CLP', u'TCL', u'HSL', u'DCA', u'HSV', u'MQT', u'RIC', u'IAN', u'KNK', u'OFK', u'HAE', u'OAJ', u'GPZ', u'GPT', u'KNW', u'BNA', u'HBB', u'PHO', u'OME', u'PHL', u'NIB', u'PHF', u'MEM', u'PHX', u'CRP', u'AET', u'TOG', u'AEX', u'EMK', u'SKK', u'WSX', u'WNA', u'MFE', u'BUR', u'TCT', u'MFR', u'GEG', u'GSO', u'BUF', u'MHK', u'JGC', u'YKM', u'FOD', u'FOE', u'NNL', u'DDC', u'MHT', u'WWT', u'QWM', u'ATY', u'RNO', u'WWP', u'ANC', u'QWF', u'ANI', u'MOU', u'MOT', u'ANV', u'KPC', u'QWY', u'GRB', u'PSP', u'JLN', u'LCH', u'MOD', u'DVL', u'COS', u'ILE', u'COU', u'KMO', u'HNH', u'ILM', u'HNM', u'HNL', u'ILI', u'HNS', u'COD', u'PEC', u'CID', u'ZBV', u'TVF', u'IKO', u'TVC', u'WAA', u'PIP', u'SRQ', u'SRV', u'LWT', u'OBU', u'WAS', u'WTK', u'CDB', u'CDC', u'PSM', u'BJI', u'SAV', u'CDV', u'NME', u'PLB', u'CDR', u'PSC', u'PLN', u'DFW', u'RUT', u'MKG', u'HYA', u'MKE', u'GNV', u'CIU', u'DIK', u'MKL', u'MKK', u'IYK', u'PSG', u'CVN', u'CVO', u'HYS', u'WST', u'JHW', u'CVG', u'PSE', u'AIA', u'BFF', u'MBL', u'FAY', u'TPA', u'FAR', u'FAT', u'OWB', u'SOP', u'FAI', u'PPV', u'MBS', u'KWT', u'UTO', u'SVC', u'MTJ', u'IRK', u'HPN', u'MTM', u'HPB', u'CHO', u'JAN', u'SDP', u'SDF', u'ARC', u'SDL', u'PWM', u'KWK', u'GSP', u'POU', u'GST', u'WDG', u'BOS', u'OAK', u'FWA', u'CCR', u'BOI', u'KQA', u'DRO', u'VIS', u'FSD', u'DRG', u'PIH', u'LYU', u'HKY', u'PIA', u'PIB', u'MYR', u'MYU', u'PIE', u'UIN', u'SXP', u'PIZ', u'HKB', u'PIR', u'PIT', u'CYF', u'BQK', u'FSM', u'WMK', u'WMH', u'WMO', u'JVL', u'MOB', u'SVS', u'KVC', u'KVL', u'EAT', u'GJT', u'LKE', u'MWA', u'EEN', u'FLL', u'FLO', u'BZN', u'DEC', u'FLG', u'SCM', u'SCK', u'PTH', u'AMA', u'JMS', u'ROC', u'MNT', u'PTA', u'KLL', u'PTU', u'ROW', u'TRI', u'VDZ', u'BDL', u'MDH', u'EWR', u'PBI', u'KCG', u'MPB', u'LRD', u'KCC', u'KCL', u'AIY', u'AVP', u'AVL', u'KLW', u'HTS', u'ACK', u'SUN', u'MLU', u'XNA', u'ZRF', u'KUK', u'ACV', u'ACT', u'IDA', u'CGI', u'TEK', u'BKC', u'CGA', u'TEX', u'CGX', u'BKW', u'PML', u'BKX', u'RDU', u'MCO', u'ELI', u'GNU', u'ELM', u'ELD', u'SJU', u'RDD', u'RDG', u'RDM', u'SJC', u'ELP', u'ELV', u'ADK', u'ART', u'LEB', u'GDV', u'BRW', u'MEI', u'BRO', u'MCG', u'BRL', u'NKI', u'LEX', u'BRD', u'CIC', u'TWA', u'TWF', u'DEN', u'MSY', u'AZO', u'CIK', u'LWS', u'YNG', u'MSS', u'EEK', u'MSP', u'MSO', u'MSN', u'MSL', u'QCE', u'LWB', u'SGY', u'MWH', u'TXK', u'DAB', u'RKS', u'SGU', u'RKD', u'SEA', u'MVY', u'EAR', u'EAU', u'DAY', u'SGF', u'KLG', u'HON', u'HOM', u'CNY', u'HOT', u'HOU', u'ESC', u'TNC', u'CNM', u'CNK', u'TNK', u'ICT', u'KGX', u'TKA', u'OOK', u'PFN', u'SCE', u'ROA', u'KGK', u'HHH', u'TEH']
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