for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    odd,even=0,0
    for i in lis:
        if(i&1):
            odd+=1
        else:
            even+=1
    if(odd%2==0 and even%2==0):
        print("YES")
    else:
        lis.sort()
        flag=0
        for i in range(n-1):
            if(lis[i+1]-lis[i]==1):
                flag=1
                break
        print("YES") if(flag) else print("NO")