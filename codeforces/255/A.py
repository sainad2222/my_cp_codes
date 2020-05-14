n = int(input())
lis = list(map(int,input().split()))
chest,bic,back=0,0,0
for i in range(0,len(lis),3):
    chest+=lis[i]
for i in range(1,len(lis),3):
    bic+=lis[i]
for i in range(2,len(lis),3):
    back+=lis[i]
if(chest>=bic and chest>=back):
    print("chest")
elif(bic>=chest and bic>=back):
    print("biceps")
else:
    print("back")