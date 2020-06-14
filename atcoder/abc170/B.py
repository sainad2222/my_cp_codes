x,y=map(int,input().split())
for i in range(101):
    if(4*i+2*(x-i)==y and x-i>=0):
        print("Yes")
        exit()
print("No")