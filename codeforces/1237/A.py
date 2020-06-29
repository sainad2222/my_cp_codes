plus = True
for _ in range(int(input())):
    n = int(input())
    if n&1==0:
        print(n//2)
    else:
        if plus:
            print((n//2)+1)
        else:
            print(n//2)  
        plus = not plus      