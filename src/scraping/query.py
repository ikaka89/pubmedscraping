'''
Created on Jan 15, 2017

@author: akshaykakumanu
'''

import xml.etree.ElementTree as ET

baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
esearch = "esearch.fcgi"
einfo = "einfo.fcgi"
db="pubmed"
datafield="[Date - Publication]"
retmax=100000;

def query_string(cls,year):
    queryParts = []
    queryParts.append(baseurl) # first, add the base eutil url
    queryParts.append(esearch) # second, the eutil tool name
    queryParts.append("?db=");
    queryParts.append(db);
    queryParts.append("&term=");
    queryParts.append(year);
    queryParts.append(" : \"3000\"[Date - Publication]")
    retstart=0
    
    #3 run einfo to get total number of records
    queryParts[1] = einfo
    infoQuery = einfo.join("")
    
    
    
    
    
    
    
    
    