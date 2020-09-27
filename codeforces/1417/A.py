for _ in range(int(input())):
    n, k = map(int, input().split())
    lis = list(map(int, input().split()))
    lis.sort()
    count = 0
    mi = lis[0]
    for i in range(1, n):
        if k>lis[i]:
            count += ((k-lis[i]) // mi)
    print(count)