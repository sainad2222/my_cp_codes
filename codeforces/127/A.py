import math
n,k=map(int,input().split())
prev1,prev2 = map(int,input().split())
total = 0
for i in range(1,n):
    tmp1,tmp2=map(int,input().split())
    total+=math.sqrt((tmp1-prev1)**2+(tmp2-prev2)**2)
    prev1,prev2 = tmp1,tmp2
print(total*k*0.02)