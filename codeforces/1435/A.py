for _ in range(int(input())):
	n = int(input())
	lis = list(map(int, input().split()))
	lis.reverse()
	print(*map(lambda x: - x, lis[:n // 2]), *lis[n // 2:])