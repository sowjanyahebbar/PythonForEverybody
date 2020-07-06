import re
a=input('file name: ')
b=open(a)


s=0

for i in b:
    i=i.rstrip()
    num=re.findall('[0-9]+',i)
    for j in num:
        s=s+int(j)

print(s)
