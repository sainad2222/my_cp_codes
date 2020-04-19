n,a = map(int,input().split())
lis = list(map(int,input().split()))
if(n>=sum(lis)):
    print(n-sum(lis))
else:
    print(-1)