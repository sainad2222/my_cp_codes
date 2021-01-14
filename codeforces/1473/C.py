def calc(n, k):
    arr = []
    cur = n - k
    while cur > 0:
        arr.append(k - cur)
        cur -= 1
    arr = [x for x in range(1, k + 1)] + arr[::-1]
    return arr


for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = calc(n, k)
    idx = lis.index(k)
    vis = set()
    idx += 1
    tmpi = idx
    while idx < n:
        vis.add(lis[idx])
        idx += 1
    i = 0
    while i < k:
        if i + 1 not in vis:
            print(i + 1, end=" ")
        i += 1
    while tmpi < n:
        print(lis[tmpi], end=" ")
        tmpi += 1
    print()
