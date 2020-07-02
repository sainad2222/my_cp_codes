def noOfDigits(n):
    n = str(n)
    return len(n)
n,t=map(int,input().split())
if noOfDigits(t)>n:
    print(-1)
    exit()
while noOfDigits(t)!=n:
    t *=10
print(t)