lis = list(map(int,input().split()))
x = {}
for i in lis:
    if i not in x:
        x[i]=1
    else:
        x[i]+=1
tmp = []
flag=0
for i in x:
    if(x[i]!=4):
        tmp.append(i)
    if(x[i]>=4):
        flag=1
if(len(set(tmp))==1 and flag):
    print("Elephant")
elif(len(set(tmp))==2 and flag):
    print("Bear")
else:
    print("Alien")