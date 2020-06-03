n,m=map(int,input().split())
x={}
for i in range(m):
    a,b=map(str,input().split())
    x[a]=b
lis = input().split()
res=[]
for i in lis:
    if(len(i)<=len(x[i])):
        res.append(i)
    else:
        res.append(x[i])
print(' '.join(res))