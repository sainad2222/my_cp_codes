from collections import defaultdict
left = defaultdict(int)
right = defaultdict(int)
n = int(input())
for _ in range(n):
    l,r = map(int,input().split())
    left[l] += 1
    right[r] += 1
print(n-max(left.values())+n-max(right.values()))
