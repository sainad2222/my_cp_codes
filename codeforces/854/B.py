n, k = map(int, input().split())
if 1 <= k < n:
    print(1,min(n-k,2*k))
else:
    print(0, min(n - k, 2 * k))