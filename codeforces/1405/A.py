for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    lis = lis[::-1]
    print(*lis)