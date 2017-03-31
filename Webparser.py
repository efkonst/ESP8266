import urllib2
import json,sys,csv


class Webparser:
    def __init__(self,stock_name):
        self.stockname = stock_name 
    
    
    
    def getmaxprices(self):
        url = 'https://www.google.com/finance/historical?output=csv&q='+self.stockname
#        proxy = urllib2.ProxyHandler({'https': '10.159.68.132:8080'})
#        opener = urllib2.build_opener(proxy)
#        urllib2.install_opener(opener)
        response = urllib2.urlopen(url)
        cr = csv.reader(response)
        csvlist = list(cr)
        pricelist = (csvlist[1:128])[::-1]
        maxlist =  [x[4] for x in pricelist]
        return maxlist

        




#w = Webparser("NOK") 
#print w.getmaxprices()

'''
stockname = "NOK"

url = 'https://www.google.com/finance/historical?output=csv&q='+stockname
response = urllib2.urlopen(url)
cr = csv.reader(response)
csvlist = list(cr)
'''
