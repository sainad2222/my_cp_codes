a = input()
b = input()
x = {}
for i in a:
    if i not in x:
        x[i]=1
    else:
        x[i]+=1
for i in b:
    if i not in x:
        x[i]=1
    else:
        x[i]+=1
y={}
s = input()
for i in s:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
print("YES") if(x==y) else print("NO")