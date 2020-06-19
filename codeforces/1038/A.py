n,k=map(int,input().split())
s = input()
x = {}
lis = [chr(65+x) for x in range(k)]
for i in lis:
    if i not in s:
        print(0)
        exit()
for i in s:
    if i not in x:
        x[i]=1
    else:
        x[i]+=1
res = list(x.values())
print(min(res)*k)