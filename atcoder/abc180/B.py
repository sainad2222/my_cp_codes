import math
n = int(input())
lis = list(map(int,input().split()))
lis = [abs(x) for x in lis]
man = sum(lis)
euc = sum([x ** 2 for x in lis])
euc = math.sqrt(euc)
cheb = max(lis)
print(man)
print(euc)
print(cheb)