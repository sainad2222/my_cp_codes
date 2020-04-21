for _ in range(int(input())):
    n = int(input())
    lis = [0]*n;x=0
    if(n%4==0):
        for i in range(int(n//2)):
            x +=2
            lis[i]=x
        for i in range(n-2,int(n//2)-1,-1):
            lis[i] = lis[i-(n//2)]-1
        lis[n-1] = lis[int(n//2)-1] + (n//2)-1
        print("YES")
        for i in lis:
            print(i,end=" ")
    else:
        print("NO")
