import math
k,n,s,p=map(int,input().split())
sheets = k*math.ceil(n/s)
print(math.ceil(sheets/p))