for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    lis.sort()
    print(max(
        lis[0]*lis[1]*lis[-3]*lis[-2]*lis[-1],
        lis[0]*lis[1]*lis[2]*lis[3]*lis[-1],
        lis[1]*lis[2]*lis[3]*lis[4]*lis[0],
        lis[-1]*lis[-2]*lis[-3]*lis[-4]*lis[-5],
    ))