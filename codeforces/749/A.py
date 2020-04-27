n  = int(input())
count=0;count2=0
while(n>0):
    if(n==3):
        n-=3
        count2+=1
    else:
        n-=2
        count+=1
print(count+count2)
for i in range(count):
    print(2,end=" ")
if(count2):
    print(3)