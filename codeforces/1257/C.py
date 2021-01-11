from collections import defaultdict, deque
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    dic = defaultdict(deque)
    for i, elem in enumerate(lis):
        dic[elem].append(i)
    ans = float('inf')
    for elem in dic:
        arr = dic[elem]
        i = 1
        t = len(arr)
        while i < t:
            ans = min(ans, arr[i] - arr[i - 1] + 1)
            i += 1
    print(ans) if ans != float('inf') else print(-1)
