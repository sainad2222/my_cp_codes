from collections import Counter
def unique(lis):
    prev = -1
    res = []
    for i in lis:
        if i != prev:
            res.append(i)
            prev = i
    return res
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    lis = unique(lis)
    dic = Counter(lis)
    mi = float('inf')
    for i in dic:
        ans = dic[i] + 1
        if lis[0] == i:
            ans -= 1
        if lis[-1] == i:
            ans -= 1
        mi = min(mi, ans)
    print(mi)