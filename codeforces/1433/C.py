for _ in range(int(input())):
	n = int(input())
	lis = list(map(int, input().split()))
	if max(lis)!=min(lis):
		idx = lis.index(max(lis))
		i = idx
		while i < n-1 and lis[i] == lis[i + 1]:
			i += 1
		if i >= n-1 :
			i = idx
			while i >0 and lis[i] == lis[i - 1]:
				i -= 1
		print(i+1)

	else:
		print(-1)