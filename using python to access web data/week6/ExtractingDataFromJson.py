import urllib.request,urllib.parse,urllib.error
import ssl
import json

#ignore ssl certificate errors

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter location: ')
print('Retrieving ',url)
html=urllib.request.urlopen(url,context=ctx).read()
print('Retrieved ',len(html),' characters')

info=json.loads(html)
info=info['comments']
print('Count: ',len(info))
Sum=0
for item in info:
    j=item['count']
    Sum=Sum+int(j)
print('Sum: ',Sum)
