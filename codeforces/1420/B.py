from bisect import bisect_right
from math import comb
def calc(n):
    return len('{0:b}'.format(n))

for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    lis.sort()
    ans = 0
    for i in range(n):
        l = calc(lis[i])
        req = pow(2, l) - 1
        tmp = bisect_right(lis, req, lo=i, hi=n)
        ans += tmp-i-1
        # print(i,tmp,ans)
    print(ans)