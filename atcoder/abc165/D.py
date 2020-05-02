a,b,n = map(int,input().split())
if(n<b):
    n=n
else:
    n=b-1
F = (a*n)//b
print(int(F))