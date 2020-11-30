# NTFS: neal
for _ in range(int(input())):
	n = int(input())
	jumps = 0
	cur = 0
	while cur < n:
		jumps += 1
		cur += jumps
	if cur == n+1:		# don't know why
		jumps += 1
	print(jumps)