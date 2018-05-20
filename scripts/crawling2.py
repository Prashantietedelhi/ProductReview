import urllib
import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse
from lxml import html
def searchDDG(site,query,pageIndex=0):
    link = "https://duckduckgo.com/?q="
    siteQuery = "+site:"+site
    url = 'https://duckduckgo.com/html/'
    params = {
                'q':query+siteQuery,
                's':0,
            }
    data = urllib.urlencode(params)
    req = urllib2.Request(url.encode(),data,headers={'User-Agent':'Mozilla/5.0'})
    response = urllib2.urlopen(req)
    htmlcont = response.read()
    return htmlcont

def getLinkContent(htmlcont,urldomain):
    soup = BeautifulSoup(htmlcont,'html.parser')
    data=[]
    for link in soup.find_all('a'):
        href = link.get('href')
        if href != None:
            parsed_uri = urlparse(link.get('href'))
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            if urldomain in domain:
                data.append((link.get_text(),link.get('href')))
    return data

def getLinkContent2(htmlcont,urldomain):
    tree = html.fromstring(htmlcont)
    print(tree)
    tree_xpath_data = tree.xpath('//*[@class="result results_links_deep highlight_d"]')
    print(tree_xpath_data)
    # data = []
    # for d in tree_xpath_data:
    #     data.append(())




def get_reviews(url):
    pass

if __name__=="__main__":
    htmlcont = (searchDDG("flipkart.com","videocon washing machine"))
    data = getLinkContent2(htmlcont,"flipkart.com")
    print(data)