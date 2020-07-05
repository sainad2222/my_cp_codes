def limit(i,j):
    limitt = 4
    if i==0: limitt-=1
    if i==n-1: limitt-=1
    if j==0: limitt-=1
    if j==m-1: limitt-=1
    return limitt

for _ in range(int(input())):
    n,m=map(int,input().split())
    res = []
    for i in range(n):
        tmplist = list(map(int,input().split()))
        res.append(tmplist)
    flag = 1
    for i in range(n):
        for j in range(m):
            limitt = limit(i,j)
            if res[i][j]>limitt:
                flag=0
                break
    if(flag==0):
        print("NO")
    else:
        print("YES")
        for i in range(n):
            for j in range(m):
                print(limit(i,j),end=" ")
            print()
    