n = int(input())
mod = 1000000007
if n == 1:
    print(0)
    exit()
print((((pow(10,n,mod)+pow(8,n,mod))%mod)-2*pow(9,n,mod))%mod)