n = int(input())
s = input().lower()
x={}
for i in s:
    if i not in x:
        x[i]=1
print("YES") if(len(x)==26) else print("NO")