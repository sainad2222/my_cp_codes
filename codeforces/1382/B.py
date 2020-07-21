for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    for i in range(n):
        if lis[i] != 1:
            break
    print("First") if i&1==0 else print("Second")