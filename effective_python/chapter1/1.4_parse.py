#-*- coding:utf-8 -*-

from urllib.parse import parse_qs

test_url = 'https://www.baidu.com/s?wd=parse_qs&rsv_spt=1&rsv_iqid=0xb7422a250002ee91&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&inputT=2135&rsv_t=cf63GDDDg72yY6sDQI%2F%2BgB%2BfqW%2BbgHGCIDRR41DofCmty30dcLc83MVwDshBfbe7ZE7p&oq=missing%2520function%2520docstring&rsv_pq=dd18a0cb000334eb&rsv_sug3=28&rsv_sug1=22&rsv_sug7=101&rsv_sug2=0&rsv_sug4=2136'

my_values = parse_qs(test_url, keep_blank_values=True)

print(repr(my_values))

ie = my_values.get('iee') or 0
print(ie)
