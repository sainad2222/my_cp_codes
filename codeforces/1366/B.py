for _ in range(int(input())):
    n,x,m = map(int,input().split())
    l = x
    r = x
    for i in range(m):
        a,b = map(int,input().split())
        if b<l or a>r:
            continue
        l = min(l,a)
        r = max(r,b)
    print(r-l+1)