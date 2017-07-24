import re
import urllib.request

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


def link_crawler(seed_url,link_regx):
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        print('--------',url)
        html = download1(url)
        for link in get_Links(html):
            if re.match(link_regx,link):
                link = urllib.parse.urljoin()
                crawl_queue.append(link)

def get_Links(html):
    webpage = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage.findall(html)


link_crawler('http://127.0.0.1:8000/places','/default/(index/view)')