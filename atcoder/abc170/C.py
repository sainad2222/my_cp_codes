x,n=map(int,input().split())
lis = []
if(n!=0):
    lis = list(map(int,input().split()))
ans = 0
msf = 1000
for i in range(101):
    tmp1 = x-i
    if tmp1 not in lis:
        print(x-i)
        exit()
    tmp2 = x+i
    if tmp2 not in lis:
        print(x+i)
        exit()