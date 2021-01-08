from collections import Counter
n = int(input())
lis = list(map(int, input().split()))
counter = Counter(lis)
print(max(list(counter.values())))
