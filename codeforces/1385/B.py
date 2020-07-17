for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    visited = []
    for i in lis:
        if i not in visited:
            visited.append(i)
    print(" ".join(map(str,visited)))