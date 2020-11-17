from collections import defaultdict,deque
for _ in range(int(input())):
    n, W = map(int, input().split())
    w = list(map(int, input().split()))
    dic = defaultdict(deque)
    for i,elem in enumerate(w):
        dic[elem].append(i+1)
    w = sorted(w, reverse=True)
    tmpW = W
    res = []
    i = 0
    while i < n and W:
        if w[i] <= W:
            W-=w[i]
            res.append(dic[w[i]].popleft())
        i += 1
    if W<=tmpW//2:
        print(len(res))
        print(*res)
    else:
        print(-1)