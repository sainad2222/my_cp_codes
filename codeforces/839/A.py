n,k=map(int,input().split())
lis = list(map(int,input().split()))
bank=0
count=0
for i in lis:
    if(k<=0):
        break
    if(bank+i>8):
        k-=8
        count+=1
        bank=bank+i-8
    else:
        k=k-(bank+i)
        count+=1
        bank=0
print(count) if(k<=0) else print(-1)