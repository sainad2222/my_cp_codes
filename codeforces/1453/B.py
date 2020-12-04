for _ in range(int(input())):
	n = int(input())
	lis = list(map(int, input().split()))
	ans = float('inf')

	# Initial
	init = 0
	for i in range(1, n):
		init += abs(lis[i] - lis[i - 1])
	
	# 1st element corner case
	tmp = init - abs(lis[0] - lis[1])
	ans = min(ans, tmp)

	# All other elements except last
	for i in range(1, n-1):
		tmp = init
		tmp -= abs(lis[i] - lis[i - 1]) + abs(lis[i] - lis[i + 1])  # If every element replace by prev element
		tmp += abs(lis[i + 1] - lis[i - 1])
		ans = min(ans, tmp)
	
	# Last element
	tmp = init - abs(lis[-2] - lis[-1])
	ans = min(ans, tmp)
	print(ans)