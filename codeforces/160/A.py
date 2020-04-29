n = int(input())
lis = list(map(int,input().split()))
lis.sort()
lis.reverse()
ans = 0;coins=0
value = sum(lis)//2
for i in lis:
    if(coins<=value):
        coins+=i
        ans+=1
print(ans)