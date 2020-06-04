def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n>>= 1
    return count

for _ in range(int(input())):
    n=int(input())
    print(2*n-countSetBits(n))