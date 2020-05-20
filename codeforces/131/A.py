s=input()
upp=0
for i in s:
    if i.isupper():
        upp+=1
if(upp==len(s) or (upp==len(s)-1 and s[0].islower())):
    ans=''
    for i in s:
        if(i.isupper()):
            ans+=i.lower()
        else:
            ans+=i.upper()
    print(ans)
else:
    print(s)