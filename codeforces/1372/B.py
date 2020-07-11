import math
def factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x//i != i: 
                result.append(x//i)
        i += 1
    return result
def lcm(a,b):
    return (a*b)//math.gcd(a,b)
for _ in range(int(input())):
    n = int(input())
    factor = factors(n)
    factor.sort()
    ans = 1e18
    aans = 1
    bans = 1
    for i in factor:
        if i==n:
            break
        a = i 
        b = n-i
        tmp = lcm(a,b)
        if min(ans,tmp)==tmp:
            aans = a
            bans = b
            ans = min(ans,tmp)
    print(aans,bans)