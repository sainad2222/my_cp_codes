for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(-1)
        continue
    print(2,end="")
    for i in range(n-1):
        print(3,end="")
    print()