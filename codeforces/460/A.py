n,m=map(int,input().split())
days=0
dayList = [m*i for i in range(1,101)]
while(n>0):
    days+=1
    n=n-1
    if days in dayList:
        n=n+1
print(days)