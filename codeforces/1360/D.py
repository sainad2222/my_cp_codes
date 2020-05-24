def SieveOfEratosthenes(n): 
    i=2
    factors=[]
    while(i*i<=n):
        if(n%i==0):
            factors.append(i)
            factors.append(n//i)
        i+=1
    return factors
for _ in range(int(input())):
    n,k=map(int,input().split())
    if(n<=k):
        print(1)
    else:
        factors = SieveOfEratosthenes(n)
        if(len(factors)==0):
            print(n)
        else:
            factors.sort()
            i=len(factors)-1
            while(factors[i]>k and i>=0):
                i-=1
            if(i<0):
                print(n)
            else:
                print(n//factors[i])