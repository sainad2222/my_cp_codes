n = int(input())
if n & 1:
    print(0)
else:
    n //= 2
    print((n-1)//2)