n = int(input())
lis = list(map(int,input().split()))
x={}
for i,j in zip(lis,range(1,n+1)):
    x[j]=i

x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

print(' '.join(map(str,list(x.keys()))))