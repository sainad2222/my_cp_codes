import math
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    if(n//k>=m):
        print(m)
    else:
        ma = n//k
        ma2 = math.ceil((m - ma)/(k-1))
        print(ma-ma2)