s = input()
ans = ''
while s and len(s)>1:
    if s[0]==".":
        ans+='0'
        s = s[1:]
    elif s[0]=='-' and s[1]=='.':
        ans += '1'
        s = s[2:]
    else:
        ans += '2'
        s = s[2:]
if len(s)!=0:
    ans+='0'
print(ans)