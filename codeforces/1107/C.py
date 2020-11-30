n, k = map(int, input().split())
lis = list(map(int, input().split()))
s = list(input())
i = 0
ans = 0
while i<n:
	j = i
	tmp = []
	while j<n and s[j]==s[i]:
		tmp.append(lis[j])
		j+=1
	tmp = sorted(tmp,reverse=True)
	ans += sum(tmp[:k])
	i = j
print(ans)
