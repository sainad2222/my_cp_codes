for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    if sum(array) == 0:
        print("NO")
    else:
        print("YES")
        if sum(array) < 0:
            print(*sorted(array))
        else:
            print(*sorted(array,reverse=True))