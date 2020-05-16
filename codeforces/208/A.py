s = input()
s=s.replace('WUB',' ')
while(s[0]==' '):
    for i in s:
        if(i==' '):
            s=s.replace(i,'',1)
        else:
            break
s=s[::-1]
while(s[0]==' '):
    for i in s:
        if(i==' '):
            s=s.replace(i,'',1)
        else:
            break
s=s[::-1]
print(s)