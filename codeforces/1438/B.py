for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    if len(b)!=len(set(b)):
        print("YES")
    else:
        print("NO")