for _ in range(int(input())):
    n = int(input())
    tmp = list(map(int,input().split()))
    lis = list(set(tmp))
    ans=-1
    flag=0
    for i in range(1,1026):
        tmp2=[]
        for j in lis:
            tmp2.append(i^j)
        if(set(tmp2)==set(lis)):
            ans=i
            flag=1
            break
    if(flag==0):
        print(-1)
    else:
        print(ans)