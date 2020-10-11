def ceil(a, b):
    return (a + b - 1) // b

for _ in range(int(input())):
    n = int(input())
    print(2)
    orign = n
    count = 1
    print(n, n - 1)
    cur = ceil(n + n - 1, 2)
    n -= 1
    while count != orign - 1:
        cur = ceil(cur + n, 2)
        n -= 1
        print(cur,n)
        count += 1