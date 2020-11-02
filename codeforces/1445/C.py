# NTFS: galen_colin
## Suppose q = 2^x*3^y*5^z then we can remove all 2's and multiply (x-1) 2's in p
## so that it is not divisible by q.
## Do the same for y,z too and take max of them
from collections import defaultdict


# prime factorization seive
def seive(n):
    dic = defaultdict(int)
    i = 2
    tmp = n
    while i * i <= tmp:
        count = 0
        while n % i == 0:
            n = n // i
            count += 1
        if count:
            dic[i] = count
        i += 1
    if n - 1:
        dic[n] = 1
    return dic


for _ in range(int(input())):
    p, q = map(int, input().split())
    if p % q:
        print(p)
        continue
    factors = seive(q)
    ans = 1
    for fact in factors:  # Iterating over all factors
        tmp = p  # Starting with p remove all facts
        while tmp % fact == 0:
            tmp = tmp // fact
        tmp = tmp * (fact**(factors[fact] - 1))  # multiply (x-1) facts again
        ans = max(ans, tmp)  # take max of all facts
    print(ans)