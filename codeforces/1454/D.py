from collections import defaultdict
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
    
def isPrime(n):
    if n==1:
        return False
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True

def recur(n,prev,prime):
    if n <= 1:
        return 
    i = prime
    flag = 0
    while i * i <= n:
        if n % i == 0 and i % prev == 0:
            flag = 1
            res.append(i)
            break
        i += 1
    if flag:
        recur(n // i, i,prime)
    else:
        if res:
            tmp = res.pop()
            if n % tmp != 0:
                res.append(tmp * n)
            else:
                res.append(tmp)
                res.append(n)
    

for _ in range(int(input())):
    n = int(input())
    if isPrime(n):
        print(1)
        print(n)
        continue
    factors = primeFactors(n)
    ans = -1
    fin = []
    for prime in factors:
        res = []
        recur(n, 1, prime)
        if len(res) > len(fin):
            fin = res[:]
    print(len(fin))
    print(*fin)