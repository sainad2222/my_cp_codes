n = int(input())
if(n&1):
    print(-1)
else:
    for i in range(n//2):
        print(2*(i+1),2*(i+1)-1,end=" ")