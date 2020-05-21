s,n=map(int,input().split())
x={}
for i in range(n):
    tmp1,tmp2=map(int,input().split())
    if tmp1 not in x:
        x[tmp1]=tmp2
    else:
        x[tmp1]+=tmp2
x={v:k for v,k in sorted(x.items()) }
for i in x.keys():
    if i<s:
        s+=x[i]
    else:
        print("NO")
        exit(0)
print("YES")