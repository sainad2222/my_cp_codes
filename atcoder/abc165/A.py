k = int(input())
lis = [k*i for i in range(1,1001)]
a,b = map(int,input().split())
flag=0
for i in lis:
    if(a<=i and i<=b):
        flag=1
        break
if(flag):
    print("OK")
else:
    print("NG")