n, m, x, y = map(int, input().split())
for i in range(y, 0, -1):
    print(x, i)
for k in range(y+1, m + 1):
    print(x, k)
for i in range(x - 1, 0, -1):
    for j in range(k, 0, -1):
        print(i,j)
    for j in range(k + 1, m + 1):
        print(i, j)
    k = j
for i in range(x + 1, n + 1):
    for j in range(k, 0, -1):
        print(i,j)
    for j in range(k + 1, m + 1):
        print(i, j)
    k = j