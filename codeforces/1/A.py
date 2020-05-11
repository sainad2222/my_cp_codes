import math
n,m,a=map(int,input().split())
nC = math.ceil(n/a)
mC = math.ceil(m/a)
print(nC*mC)