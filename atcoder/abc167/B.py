a,b,c,k=map(int,input().split())
value=0
n = k-a
if(n<=0):
    value=k
else:
    value = a
if(n>0):
    n = n-b
if(n>0):
    value = value - n
print(value)