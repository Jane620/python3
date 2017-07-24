import urllib.request
import itertools

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


for page in itertools.count(1):
    max_error = 5
    num_error = 0
    url = 'http://127.0.0.1:8000/places/default/view/-%d'% page
    html = download1(url)
    if html is None:
        num_error += 1
        if num_error == max_error:
            break
    else:
        num_error = 0
        pass
