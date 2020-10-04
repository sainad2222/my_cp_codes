ans = ''
res = -float('inf')
for _ in range(int(input())):
    s = input().split()
    cur = sum(list(map(int, s[3:]))) + int(s[1]) * 100 - int(s[2]) * 50
    if cur >= res:
        ans = s[0]
    res = max(cur, res)
print(ans)