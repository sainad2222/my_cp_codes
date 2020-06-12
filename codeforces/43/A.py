n = int(input())
x={}
for i in range(n):
    s = input()
    if s not in x:
        x[s]=1
    else:
        x[s]+=1
ma = -1
ans = ''
for i in x:
    if x[i]>ma:
        ma = x[i]
        ans = i
print(ans)