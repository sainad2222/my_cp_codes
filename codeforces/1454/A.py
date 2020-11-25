for _ in range(int(input())):
    n = int(input())
    print(*[x+1 for x in range(1,n)],1)