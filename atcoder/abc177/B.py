s = input()
t = input()
n = len(s)
m = len(t)
def check(s, t):
    count = 0
    for i, j in zip(s, t):
        if i == j:
            count += 1
    return count
ans = -1
for i in range(n - m + 1):
    tmp = s[i:i + m]
    count = check(tmp, t)
    ans = max(ans, count)
print(m-ans)