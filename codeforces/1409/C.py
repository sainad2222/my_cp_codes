for _ in range(int(input())):
    n, x, y = map(int, input().split())
    dic = {}
    i = 1
    while i <n:
        if (y - x) % (n - i) == 0:
            break
        i += 1
    diff = (y - x) // (n - i)
    res = []
    cur = x
    while cur <= y:
        res.append(cur)
        cur += diff
    l = len(res)
    rem = n - l
    tmp = rem
    cur = x
    count = 0
    while rem and cur-diff>0:
        rem -= 1
        cur -= diff
        res.append(cur)
        count += 1
    # print(rem,count)
    rem = (tmp - count)
    # print(rem)
    cur = y
    while rem:
        cur += diff
        res.append(cur)
        rem -= 1
    print(*res)