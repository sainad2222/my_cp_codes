t = int(input())
for _ in range(t):
	[n,k] = list(map(int, input().split()))
	for i in range(2, n + 1):
		if(n % i == 0):
			print(n + i + (2 * (k - 1)))
			break