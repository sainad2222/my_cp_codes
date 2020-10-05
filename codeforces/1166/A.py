from collections import defaultdict
n = int(input())
dic = defaultdict(lambda : 0)
for i in range(n):
    s = input()
    dic[s[0]] += 1
ans = 0
for i in dic.values():
    j = i // 2
    i -= j
    ans += (i * (i - 1) + j * (j - 1))
print(ans//2)