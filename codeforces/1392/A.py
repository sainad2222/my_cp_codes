for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    if len(set(lis)) > 1:
        print(1)
    else:
        print(n)