for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = list(map(int, input().split()))
    lis.sort()
    flag = 1
    for i in lis:
        if i > k:
            flag = 0
            break
    if flag:
        print("YES")
        continue
    if lis[0] + lis[1] <= k:
        print("YES")
    else:
        print("NO")
