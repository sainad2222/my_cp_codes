n = int(input())
x={}
for i in range(n):
    s = input()
    if s not in x:
        x[s]=1
    else:
        x[s]+=1
count=0
for i in x:
    count+=1
print(count)