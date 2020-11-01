for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = 0
    init = s.count('L')

    for i in range(1, n):
        if s[i] == "W" and s[i - 1] == "W":
            ans += 2
        elif s[i] == "W":
            ans += 1
    if s[0] == 'W':
        ans += 1

    if k == 0:
        print(ans)
        continue

    final = []
    tmp = s.find('W')
    count = 0
    for i in range(tmp + 1, n):
        if s[i] == 'L':
            count += 1
        else:
            final.append(count)
            count = 0
    tmp3 = []
    for i in final:
        if i != 0:
            tmp3.append(i)
    final = tmp3[:]
    final.sort()
    i = 0
    while k > 0 and i < len(final):
        if final[i] <= k:
            k -= final[i]
            ans += 2 * final[i]
            ans += 1
        else:
            ans += 2 * k
            k = 0
        i += 1
    if 'W' not in s:
        if k<=n:
            ans += 2 * k - 1
        else:
            ans += 2 * n - 1
    else:
        ans += 2 * min(k, (init - sum(final)))
    print(ans)