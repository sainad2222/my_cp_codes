def check(n):
    n=list(str(n))
    for i in n:
        if(i=="4" or i=='7'):
            pass
        else:
            return False
    return True
lis = [x for x in range(1001) if(check(x)==True)]
n = int(input())
flag=0
for i in lis:
    if(n%i==0):
        flag=1
        break
if(flag):
    print("YES")
else:
    print("NO")