I = 1009
a,b = map(int,input().split());flag=0
for i in range(1,I):
    x = (i*8)//100;y=(i*10)//100
    if(x==a and y==b):
        print(i)
        flag=1
        break
if(flag==0):
    print(-1)