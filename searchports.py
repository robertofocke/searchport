import requests
from googlesearch import search
import re

domain=input('dominio: ')
params={'str':'ssl','db_chkbx':'IANA','db_chkbx':'WG','db_chkbx':'WP','submit':'Submit'}
site=requests.post("https://wintelguy.com/port-search/", data=params, verify=False)
patron=re.compile(r'<td valign="top">(\d*)<')
listaP=patron.findall(site.text)
for esteP in listaP:
        if esteP !='':
                query='site:/'+domain+':'+esteP+'/'
                for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)