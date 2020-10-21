# F*ck implementation problems
# Ab to kaam hoja bsdk
# Adding comments so it might be helpful to someone
## Moral: Don't watch IPL during contest
from collections import Counter
for _ in range(int(input())):
	n = int(input())
	lis = list(map(int, input().split()))
	## Check for NO condition
	counter = Counter(lis)
	if len(counter) <= 1:
		print("NO")
		continue

	print("YES")
	oneWala = [1]     # Every index a[0]!=a[idx]
	othersWala = []   # if equals then it cannot be in oneWala
	for i in range(1, n):
		if lis[i] != lis[0]:
			oneWala.append(i + 1)
		else:
			othersWala.append(i + 1)
	
	## We need to have atleast one edge from oneWala to othersWala
	## So check diff element in oneWala to connect to othersWala element
	flag = 0
	idx = -1
	for i in oneWala:
		for j in othersWala:
			if lis[i - 1] != lis[j - 1]:
				idx = i-1
				flag = 1
				break
		if flag:
			break
	## Now connect everything in oneWala to 1
	for i in oneWala:
		if i != 1:
			print(1, i)
	
	if len(othersWala) == 0:
		continue
	## Now connect everything in othersWala to othersWala[0]
	for i in othersWala:
		print(idx + 1, i)
	