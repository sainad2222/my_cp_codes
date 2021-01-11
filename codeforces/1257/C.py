# NTFS: raj1307
# Idea: min length will be between two occurences of same element so store the indices of all occurences of an element in an array and calculate min length among all of them
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
