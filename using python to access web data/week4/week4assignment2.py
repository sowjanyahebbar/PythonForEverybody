import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('enter-')
count=input('enter count-')
position=input('enter position-')
print('Retrieving: ',url)
for i in range(int(count)):
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    print('Retrieving: ',tags[int(position)-1].get('href',None))
    url=tags[int(position)-1].get('href',None)
    

