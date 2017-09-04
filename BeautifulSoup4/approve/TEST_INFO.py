#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import re,requests,xlwt
from bs4 import BeautifulSoup


str = '''
<p>
	1、金谷农商银行</p>
<p>
	2、内蒙古正大有限公司</p>
<p>
	3、德福康实业有限公司</p>
<p>
	4、蒙羊牧业股份有限公司</p>
<p>
	5、内蒙古民丰种业有限公司</p>
<p>
	6、内蒙古雪原乳业有限公司</p>
<p>
	7、内蒙古蒙酒酒业有限公司</p>
<p>
	8、内蒙古掌宝科技有限公司</p>
<p>
	9、内蒙古河套酒业有限公司</p>
<p>
	10、内蒙古蒙羊羊业有限公司</p>
<p>
	11、内蒙古西贝餐饮有限公司</p>
<p>
	12、内蒙古蒙恩乳业有限公司</p>
<p>
	13、内蒙古万润贸易有限公司</p>
<p>
	14、内蒙古老绥元餐饮有限公司</p>
<p>
	15、赤峰大吉药业集团有限公司</p>
<p>
	16、赤峰东荣羊绒制品有限公司</p>
<p>
	17、赤峰凯兰羊绒制品有限公司</p>
<p>
	18、赤峰力王工艺美术制品公司</p>
<p>
	19、呼和浩特泛蒙石材有限公司</p>
<p>
	20、内蒙古古顺园食品有限公司</p>
<p>
	21、内蒙古蒙古王酒业有限公司</p>
<p>
	22、内蒙古苏尼特肉业有限公司</p>
<p>
	23、内蒙古威尔浪服装有限公司</p>
<p>
	24、内蒙古高原杏仁露有限公司</p>
<p>
	25、内蒙古富源牧业有限责任公司</p>
<p>
	26、内蒙古八方保姆有限责任公司</p>
<p>
	27、内蒙古燕圆食品股份有限公司</p>
<p>
	28、内蒙古显鸿科技股份有限公司</p>
<p>
	29、内蒙古阴山优麦食品有限公司</p>
<p>
	30、内蒙古正观品牌顾问有限公司</p>
<p>
	31、内蒙古蒙农生态发展有限公司</p>
<p>
	32、内蒙古惠宾电子商务有限公司</p>
<p>
	33、内蒙古雅琪羊绒制品有限公司</p>
<p>
	34、内蒙古羊羊牧业股份有限公司</p>
<p>
	35、内蒙古蒙古大营餐饮有限公司</p>
<p>
	36、内蒙古鼎奇幼教联盟有限公司</p>
<p>
	37、内蒙古金田科技股份有限公司</p>
<p>
	38、内蒙古东达圣邦燕麦有限公司</p>
<p>
	39、内蒙古东鸽电器集团有限公司</p>
<p>
	40、内蒙古东绿生态股份有限公司</p>
<p>
	41、呼和浩特市精德食品有限公司</p>
<p>
	42、呼伦贝尔市龙凤集团有限公司</p>
<p>
	43、内蒙古北斗瀚海科技有限公司</p>
<p>
	44、内蒙古北平纺织有限责任公司</p>
<p>
	45、内蒙古创优投资管理有限公司</p>
<p>
	46、内蒙古汉森酒业集团有限公司</p>
<p>
	47、内蒙古华腾科技发展有限公司</p>
<p>
	48、内蒙古万民药房连锁有限公司</p>
<p>
	49、兴安盟草原盛业米业有限公司</p>
<p>
	50、内蒙古正隆谷物食品有限公司</p>
<p>
	51、内蒙古自立电脑有限责任公司</p>
<p>
	52、内蒙古漠菇生物科技有限公司</p>
<p>
	53、内蒙古蒙根花农牧业有限公司</p>
<p>
	54、内蒙古华程科贸有限责任公司</p>
<p>
	55、内蒙古鼎弘法商咨询有限公司</p>
<p>
	56、内蒙古青腾商贸有限责任公司</p>
<p>
	57、内蒙古库布其酒业有限责任公司</p>
<p>
	58、内蒙古王爷地苁蓉生物有限公司</p>
<p>
	59、内蒙古蒙众联投资咨询有限公司</p>
<p>
	60、内蒙古蒙伊萨食品有限责任公司</p>
<p>
	61、内蒙古玛希勒汽车玻璃有限公司</p>
<p>
	62、内蒙古精诚高压绝缘子有限公司</p>
<p>
	63、内蒙古大牧场牧业集团有限公司</p>
<p>
	64、内蒙古大盛业羊绒制品有限公司</p>
<p>
	65、呼和浩特市苏鲁锭皮业有限公司</p>
<p>
	66、内蒙古阿拉善苁蓉集团有限公司</p>
<p>
	67、内蒙古二龙屯有机农业有限公司</p>
<p>
	68、内蒙古谷道粮原农产品有限公司</p>
<p>
	69、内蒙古华蒙通物流控股有限公司</p>
<p>
	70、内蒙古浩源新材料股份有限公司</p>
<p>
	71、内蒙古华颐乐牧业科技有限公司</p>
<p>
	72、内蒙古草都草牧业股份有限公司</p>
<p>
	73、内蒙古哈木格文化传媒有限公司</p>
<p>
	74、内蒙古红山怡葡萄酒业有限公司</p>
<p>
	75、内蒙古蒙亮民贸(集团)有限公司内蒙古中贷金融信息服务有限公司</p>
<p>
	76、内蒙古大统体育用品股份有限公司</p>
<p>
	77、内蒙古云谷电力科技股份有限公司</p>
<p>
	78、维信(内蒙古)羊绒集团有限公司</p>
<p>
	79、内蒙古网智科技服务有限责任公司</p>
<p>
	80、内蒙古蒙都羊业食品股份有限公司</p>
<p>
	81、内蒙古蒙康圣业科技发展有限公司</p>
<p>
	82、内蒙古蒙清农业科技开发有限公司</p>
<p>
	83、内蒙古蒙元牧业食品有限责任公司</p>
<p>
	84、内蒙古康太光学眼镜连锁有限公司</p>
<p>
	85、内蒙古海德投资控股集团有限公司</p>
<p>
	86、内蒙古惠丰堂大药房连锁有限公司</p>
<p>
	87、内蒙古阿里婆婆电子商务有限公司</p>
<p>
	88、内蒙古永业农丰生物科技有限公司</p>
<p>
	89、额尔古纳市丽丽娅食品有限责任公司</p>
<p>
	90、乌兰察布市集宁国际皮革城有限公司</p>
<p>
	91、内蒙古小尾羊牧业科技股份有限公司</p>
<p>
	92、呼和浩特市蒙谷香生物科技有限公司</p>
<p>
	93、鄂尔多斯农村商业银行股份有限公司</p>
<p>
	94、呼和浩特市万盛昌水业饮料有限公司</p>
<p>
	95、内蒙古易捷贷金融信息服务有限公司</p>
<p>
	96、内蒙古正时生态农业(集团有限公司)</p>
<p>
	97、内蒙古田牧实业(集团)股份有限公司</p>
<p>
	98、内蒙古清谷新禾有机食品集团有限公司</p>
<p>
	99、包头市日盛世濠餐饮连锁管理有限公司</p>
'''

def get_html(url,flag=1):
    try:
        rep = requests.get(url)
        if flag:
            return rep.text
        else:
            return rep.content
    except Exception as e:
        return ''

def get_soup(html):
    soup = BeautifulSoup(html,'html.parser')
    return soup

def get_baike(name):
    '''
    :param name:
    :return: str
    '''
    root_url = 'https://baike.baidu.com/search/none'
    param = {'word':name,'pn':'0','rn':'10','enc':'utf8'}
    html = requests.get(root_url,params=param).content
    soup = get_soup(html)

    # 针对某些公司查询不到直接的公司,需要额外获取公司link
    p = soup.find_all('dl', attrs={'class': 'search-list'})
    if not p:
        return ''
    dd = p[0].find_next('dd')
    if dd.a.get('href'):
        root_url = dd.a.get('href')

    staff = search_baike(root_url)
    return staff

def search_baike(url):
    if not url:
        return ''
    html = get_html(url, flag=0)
    soup = get_soup(html)
    if soup.find('body'):
        str = soup.find('body').text
    else:
        str =  ''
    staff = re.findall(re.compile(r'[\d]+.?[\d]+人'), str)
    return ''.join(staff[0] if staff else '0')


def write_file(dict_info,name):
    '''
    :param dict_info:
    :param name:
    :return:
    '''
    file_path = 'resource/CompanyInfo_%s.xls' % name
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(name,cell_overwrite_ok=True)
    row0 = [u'排名', u'公司名称', u'员工数']
    worksheet.write(0, 0, row0[0])
    worksheet.write(0, 1, row0[1])
    worksheet.write(0, 2, row0[2])
    row1 = []
    for key,value in dict_info.items():
        rank = int(key.strip())
        comp_name = value[0]
        staff_count = value[1]
        row1.append([rank,comp_name,staff_count])

    for i in range(len(row1)):
        worksheet.write(i + 1, 0, row1[i][0])
        worksheet.write(i + 1, 1, row1[i][1])
        worksheet.write(i + 1, 2, row1[i][2])

    workbook.save(file_path)


def get_content(str):

    soup = get_soup(str)
    p = soup.find_all('p')
    dict_info = {}
    for i in p:
        #str = i.text.replace(u'\u3000',u' ').split()
        str = i.text.split('、')
        rank = str[0]
        name = str[1].split()
        #name = re.findall(re.compile(r'[^\\u4e00-\\u9fa5]+公司'),str[1]) or ['no name']
        dict_info[rank] = name

    dict_info2 = {}
    for key,value in dict_info.items():
        if value:
            staff = get_baike(value[0])
        else:
            staff = ''
        value.append(staff)
        dict_info2[key] = value

    return dict_info2

if __name__ == '__main__':

    content = get_content(str)
    write_file(content,'内蒙古')
