n = int(input())
ans = 0
for i in range(1,n+1):
    num = str(i)
    oc = str(oct(i))
    if '7' in num or '7' in oc:
        continue
    ans+=1
print(ans)
