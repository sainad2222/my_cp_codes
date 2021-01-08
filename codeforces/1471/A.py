def ceil(a, b):
    return (a + b - 1) // b

for _ in range(int(input())):
    n, x = map(int, input().split())
    lis = list(map(int, input().split()))
    i = 0
    bank = 0
    ans = 0
    mi = 0
    while i < n - 1:
        if (bank + lis[i]) % x == 0:
            mi += (bank + lis[i]) // x
            bank = 0
        else:
            bank += lis[i]
        i += 1
    mi += ceil(bank + lis[-1], x)
    ma = 0
    i = 0
    bank = 0
    while i < n - 1:
        if (bank + lis[i]) % x:
            ma += ceil(bank + lis[i], x)
            bank = 0
        else:
            bank += lis[i]
        i += 1
    ma += ceil(bank + lis[-1], x)
    print(mi, ma)


