for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    cur = lis[0];flag=0
    for i in range(1,n):
        if((cur-lis[i])%2!=0):
            flag=1
    if(flag==0):
        print("YES")
    else:
        print("NO")