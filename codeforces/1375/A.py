for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    for i in range(n):
        if i&1:
            print(abs(lis[i])*-1,end=" ")
        else:
            print(abs(lis[i]),end=" ")
    print()