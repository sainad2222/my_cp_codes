from collections import deque
n, k = map(int, input().split())
lis = list(map(int, input().split()))
d = deque()
su = 0
cur = 0
i = 0
while i < k:
    cur += lis[i]
    d.append(lis[i])
    i += 1
while i < n:
    su += cur
    cur -= d.popleft()
    d.append(lis[i])
    cur += lis[i]
    i += 1
su += cur
print(su / (n - k + 1))
