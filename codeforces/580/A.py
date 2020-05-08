n = int(input())
lis = list(map(int,input().split()))
stack=[];msf=-1
if(len(lis)==1):
    msf=1
    pass
for i in range(n-1):
    if(len(stack)==0):
        stack.append(lis[i])
    if(lis[i+1]>=lis[i]):
        stack.append(lis[i+1])
    if(lis[i+1]<lis[i]):
        msf = max(len(stack),msf)
        stack = []
    msf = max(len(stack),msf)
print(msf)