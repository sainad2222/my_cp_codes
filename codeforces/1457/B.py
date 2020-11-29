def ceil(a, b):
	return (a + b - 1) // b
for _ in range(int(input())):
	n,k = map(int,input().split())
	lis = list(map(int,input().split()))
	ans = float('inf')
	ma = max(lis)
	for elem in range(1, ma+1):
		i = 0
		tmp = 0
		while i < n:
			if lis[i] != elem:
				i += k
				tmp += 1
			else:
				i += 1
		ans = min(ans,tmp)
	print(ans)