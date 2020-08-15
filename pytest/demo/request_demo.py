

def request_demo():
    import requests
    url = 'http://www.baidu.com'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url,headers=header)
    print(r.status_code)


if __name__ == '__main__':
    request_demo()
    print('-------')