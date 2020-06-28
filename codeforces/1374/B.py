for _ in range(int(input())):
    n = int(input())
    count = 0
    while n!=1:
        if n%6==0:
            n=n//6
            count+=1
        elif n%3==0:
            n=n//3
            count+=2
        else:
            break
    print(count) if n==1 else print(-1)