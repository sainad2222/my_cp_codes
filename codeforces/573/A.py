# NTFS: SteelRaven

n = int(input())
lis = list(map(int,input().split()))

for i,num in enumerate(lis):
	while lis[i]%2==0:
		lis[i] = lis[i]//2
	while lis[i]%3==0:
		lis[i] = lis[i]//3
print("Yes") if all(x==lis[0] for x in lis) else print("No")
