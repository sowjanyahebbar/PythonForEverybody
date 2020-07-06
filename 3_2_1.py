import re
a=input('file name: ')
b=open(a)
#c=b.read().rstrip()

s=0
#c=b.read().rstrip()
for i in b:
    i=i.rstrip()
    num=re.findall('[0-9]+',i)
    for j in num:
        s=s+int(j)

print(s)
