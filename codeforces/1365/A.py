for _ in range(int(input())):
    n,m=map(int,input().split())
    lis = []
    # if(n==1 or m==1):
    #     flag=1
    #     for i in range(n):
    #         tmp=input()
    #         if '1' in tmp:
    #             print("Vivek")
    #             flag=0
    #     if(flag):
    #         print("Ashish")
    #     continue
    for i in range(n):
        tmp = list(map(int,input().split()))
        lis.append(tmp)
    claimedR = set()
    claimedC = set()
    for i in range(n):
        for j in range(m):
            if(lis[i][j]==1):
                claimedR.add(i)
                claimedC.add(j)
    ans = min(m-len(claimedC),n-len(claimedR))
    if(ans%2==0):
        print("Vivek")
    else:
        print("Ashish")