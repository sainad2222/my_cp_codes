for _ in range(int(input())):
	n,m,r,c = map(int,input().split())
	print(max(abs(1-r)+abs(1-c),abs(1-r)+abs(m-c),abs(n-r)+abs(1-c),abs(r-n)+abs(c-m)))
