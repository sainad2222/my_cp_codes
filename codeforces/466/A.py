n, m, a, b = map(int, input().split())
def ceil(a, b):
    return (a + b - 1) // b

if (m * a <= b):
    print(n * a)
else:
    print(min(ceil(n, m) * b, n // m * b + n % m * a))