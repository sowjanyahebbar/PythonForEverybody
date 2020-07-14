import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url')
print('Retrieving ',url)
html=urllib.request.urlopen(url,context=ctx).read()
print('Retrieved ',len(html),' characters')

tree=ET.fromstring(html)
lst=tree.findall('comments/comment')
print('Count: ',len(tree.findall('.//count')))
sum=0
for i in lst:
      j=i.find('count').text
      sum=sum+int(j)
print('Sum: ',sum)
