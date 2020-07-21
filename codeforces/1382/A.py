for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    flag = 0
    for i in a:
        if i in b:
            print("YES")
            print(1, i)
            flag = 1
            break
    if not flag:
        print("NO")