def isPrime(n):
    if n==1:
        return False
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
        continue
    if n %2 == 0:
        if n > 2:
            print(2)
        else:
            print(1)
        continue
    if isPrime(n):
        n -= 1
        if n > 2:
            print(3)
        else:
            print(2)
    else:
        print(3)