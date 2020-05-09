import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    print(k+math.ceil(k/(n-1))-1)