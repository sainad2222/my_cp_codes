for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    x={}
    for i in lis:
        if i not in x:
            x[i]=1
        else:
            x[i]+=1
    res = list(x.values())
    visited = []
    res = sorted(res,reverse=True)
    ans = 0
    for i in res:
        while(i in visited and i>0):
            i-=1
        visited.append(i)
        ans+=i
    print(ans)