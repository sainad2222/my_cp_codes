for _ in range(int(input())):
	n = int(input())
	ans = 0
	flag = 0
	for i in range(1, 10):
		for j in [1, 2, 3, 4]:
			s = int(str(i) * j)
			ans += j
			if s == n:
				flag = 1
				break
		if flag:
			break
				
	print(ans)