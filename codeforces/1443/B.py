# NTFS: Mukundan314
for _ in range(int(input())):
    a, b = map(int, input().split())
    s = input().strip("0")
    if not len(s):
        print(0)
        continue
    # init
    n = len(s)
    ans = 0
    res = []
    prev = s[0]
    count = 1

    # loop and make group
    for i in range(1, n):
        if s[i] == prev:
            count += 1
        else:
            res.append(count)
            count = 1
        prev = s[i]
    res.append(count)

    # loop over zeros and update ans accordingly
    for i in res[1::2]:
        ans += min(a, i * b)
    ans += a
    print(ans)