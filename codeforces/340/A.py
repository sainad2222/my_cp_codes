from math import gcd
x, y, a, b = map(int, input().split())
num = (x * y) // gcd(x, y)
ans = (b // num) - (a // num)
if a % num == 0:
    ans += 1
print(ans)
