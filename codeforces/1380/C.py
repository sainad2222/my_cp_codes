# This code inspired by pajenegod's code
for _ in range(int(input())):
    n,x=map(int,input().split())
    lis = list(map(int,input().split()))
    lis = sorted(lis)
    count = 0
    while lis:
        ncount = 0
        mi = 1e9
        while lis and ncount*mi<x:
            mi = lis.pop()
            ncount+=1
        if ncount*mi>=x:
            count+=1
    print(count)