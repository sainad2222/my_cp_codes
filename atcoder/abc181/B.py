def su(n):
    return (n * (n + 1)) // 2


n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += su(b) - su(a) + a
print(ans)