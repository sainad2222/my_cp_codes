n = int(input())
lis = list(map(int,input().split()))
prod = 1
if 0 in lis:
    print(0)
    exit(0)
for i in lis:
    if(prod>1000000000000000000):
        print(-1)
        exit(0)
    prod=prod*i
print(prod) if(prod<=1000000000000000000) else print(-1)