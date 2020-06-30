for _ in range(int(input())):
    a,b,c=map(int,input().split())
    ans = 1e18
    for x in -1,0,1:
        for y in -1,0,1:
            for z in -1,0,1:
                tmp1 = a+x
                tmp2 = b+y
                tmp3 = c+z
                ans = min(ans,abs(tmp1-tmp2)+abs(tmp1-tmp3)+abs(tmp3-tmp2))
    print(ans)