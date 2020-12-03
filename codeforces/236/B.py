#NTFS: neharika_shah
from collections import defaultdict
mod = 1073741824
a,b,c = map(int,input().split())

def primeFactors(n):
	dic = defaultdict(int)
	factors = []
	while n % 2 == 0:
		dic[2] += 1
		n = n // 2
	
	i = 3
	while i * i <= n:
		while n % i == 0:
			dic[i] += 1
			n = n // i
		i += 2
	
	if n > 2:
		dic[n] += 1
	return dic


def calc(n):
	res = 1
	dic = primeFactors(n)
	for val in dic.values():
		res = (res*(val+1))%mod
	return res
# print(calc(8))
ans = 0
for i in range(1,a+1):
	for j in range(1,b+1):
		for k in range(1,c+1):
			# print(calc(i*j*k))
			ans = (ans+calc(i*j*k))%mod
print(ans)
