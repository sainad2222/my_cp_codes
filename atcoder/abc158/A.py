s = input()
x={}
for i in s:
    if i not in x:
        x[i]=1
    else:
        x[i]+=1
count=0
for i in list(x.values()):
    count+=1
if(count==2):
    print("Yes")
else:
    print("No")