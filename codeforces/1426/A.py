def ceil(a, b):
    return (a + b - 1) // b
for _ in range(int(input())):
    n, x = map(int, input().split())
    if n == 1 or n==2:
        print(1)
        continue
    n -= 2
    ans = 1
    print(ceil(n,x)+1)