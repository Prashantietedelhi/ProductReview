import urllib
from urllib.parse import urlencode
from urllib.request import Request,urlopen
def searchDDG(site,query,pageIndex=0):
    link="https://duckduckgo.com/?q="
    siteQuery="+site:"+site
    url='https://duckduckgo.com/html/'
    params={
        'q':urllib.parse.urljoin(query,siteQuery),
        's':0,
    }
    data=urlencode(params)
    req=Request(url.encode(),data,headers={'User-Agent':'Mozilla/5.0'})
    response=urlopen(req)
    html=response.read()
    return html

print(searchDDG("flipkart.com","lg"))