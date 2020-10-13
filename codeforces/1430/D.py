def ceil(a, b):
    return (a + b - 1) // b
for _ in range(int(input())):
    n = int(input())
    s = input()
    streak = 1
    prev = s[0]
    res = []
    for i in range(1,n):
        if s[i] == prev:
            streak += 1
        else:
            prev = s[i]
            res.append(streak)
            streak = 1
    res.append(streak)
    ans = 0
    next_max = 0
    t = len(res)
    for i in range(t):
        next_max = max(next_max, i)
        while next_max<t and res[next_max] == 1:
            next_max += 1
        if next_max != t:
            res[next_max] -= 1
            ans += 1
        ans += 1
    print(ceil(ans,2))