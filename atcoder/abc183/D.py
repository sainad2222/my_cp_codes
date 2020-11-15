n,w=map(int,input().split())
store = [0]*(200006)
for i in range(n):
	s,e,p=map(int,input().split())
	store[s] += p
	store[e] -= p
res = [0]*(200006)
res[0] = store[0]
for i in range(1,200006):
	res[i] = store[i]+res[i-1]
for i in res:
	if i>w:
		print("No")
		break
else:
	print("Yes")