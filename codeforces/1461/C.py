# NTFS: titia
# Idea: we need to consider experiments until we encounter last unsorted element and we can keep it unsorted if we do not sort it xD
for _ in range(int(input())):
    n,m = map(int,input().split())
    lis = list(map(int,input().split()))

    idx = -1
    for i in reversed(range(n)):
        if lis[i]!=i+1:
            idx = i+1
            break
    if idx==-1:
        print(1)
        for i in range(m):
            r,p = map(float,input().split())
        continue
    
    ans = 1
    for i in range(m):
        r,p = map(float,input().split())
        r = int(r)
        if r>=idx:
            ans *= (1-p)
    print(1-ans)        # ans is actually prob of not sorted

