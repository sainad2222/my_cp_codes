for _ in range(int(input())):
	n = int(input())
	lis = list(map(int,input().split()))
	res = []
	for i in range(n):
		if not res or res[-1]==0 or (res[-1]==1 and lis[i]==0):
			res.append(lis[i])
	ans = 0
	idx = res.index(1)
	for i in range(idx+1, len(res)):
		if res[i] == 1:
			ans += (i - idx - 1)
			idx = i
	print(ans)