for _ in range(int(input())):
    n = int(input())
    flag = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if 3 * i + 5 * j + 7 * k == n:
                    print(i, j, k)
                    flag = 1
            if flag:
                break
        if flag:
            break
    if not flag:
        print(-1)
                    