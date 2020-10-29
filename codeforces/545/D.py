n = int(input())
lis = list(map(int, input().split()))
lis.sort()
# print(lis)
cur = lis[0]
count = 1
i = 1
while i < n:
    if cur <= lis[i]:
        count += 1
    else:
        while i < n and cur > lis[i]:
            i += 1
        if i < n:
            count += 1
        else:
            break
    cur += lis[i]
    i += 1
print(count)