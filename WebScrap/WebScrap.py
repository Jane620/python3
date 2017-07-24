import urllib.request
import re

def download1(url,user_agent='wswp',retry=2):
    print('download...',url)
    headers = {'User-agent':user_agent}
    request = urllib.request.Request(url,headers = headers)
    try:
        html = urllib.request.urlopen(url).read()
        html = html.decode('GBK')
    except urllib.request.URLError as e:
        print('download, error:',e.reason)
        html = None
        if retry > 0 :
            print('---',e.__getattribute__('code'))
            if hasattr(e,'code') and 500<= e.code <= 600:
                return download1(url,user_agent,retry-1)
    return html

def crawl_sitemap(url):
    sitemap = download1(url)
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html = download1(link)


#crawl_sitemap('https://freesitemapgenerator.com/sitemap.xml')
crawl_sitemap('http://127.0.0.1:8000/places/static/sitemap.xml')

