n, x, y = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort()
ans = 0
i = 0
od = True
while i < n:
    if od:
        if lis[i] <= x:
            ans += 1
        else:
            if x > y:
                ans += 1
    else:
        if lis[i] + y <= x:
            ans += 1
        else:
            if x > y:
                ans += 1

    i += 1
    od = not od
print(ans)
