n = int(input())
lis = list(map(int,input().split()))
e,o = 0,0
for i in lis:
    if(i&1):
        o+=1
    else:
        e+=1
if(e==1):
    for i in range(n):
        if(lis[i]%2==0):
            print(i+1)
            exit(0)
else:
    for i in range(n):
        if(lis[i]%2!=0):
            print(i+1)
            exit(0)