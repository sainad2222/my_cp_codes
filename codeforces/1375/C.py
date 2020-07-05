def limit(i,j):
    limitt = 4
    if i==0: limitt-=1
    if i==n-1: limitt-=1
    if j==0: limitt-=1
    if j==m-1: limitt-=1
    return limitt

for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    if lis[0]<lis[-1]:
        print("YES")
    else:
        print("NO")