n = int(input())
home,guest=[],{}
for i in range(n):
    t1,t2=map(int,input().split())
    home.append(t1)
    if t2 not in guest:
        guest[t2]=1
    else:
        guest[t2]+=1
count=0
for i in home:
    if i in guest:
        count+=guest[i]
print(count)