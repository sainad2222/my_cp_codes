n, sx, sy, ex, ey = map(int, input().split())
s = input()
x = ex - sx
y = ey - sy
ans = 0
i = 0
if x < 0:
    while x != 0 and i < n:
        if s[i] == 'W':
            x += 1
        if x == 0:
            break
        i += 1
else:
    while x != 0 and i < n:
        if s[i] == 'E':
            x -= 1
        if x == 0:
            break
        i += 1
if i >= n:
    print(-1)
    exit()
ans = max(i, ans)
i = 0
if y < 0:
    while y != 0 and i < n:
        if s[i] == 'S':
            y += 1
        if y == 0:
            break
        i += 1
else:
    while y != 0 and i < n:
        if s[i] == 'N':
            y -= 1
        if y == 0:
            break
        i += 1
if i >= n:
    print(-1)
    exit()
ans = max(i, ans)
print(ans + 1)
