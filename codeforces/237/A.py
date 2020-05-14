n = int(input())
x={}
for i in range(n):
    s = input()
    if s not in x:
        x[s]=1
    else:
        x[s]+=1
print(max(list(x.values())))