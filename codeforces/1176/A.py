for _ in range(int(input())):
    n = int(input())
    count=0;flag=1
    while(n!=1):
        if(n%2==0):
            n=n//2
            count+=1
        elif(n%3==0):
            n=2*(n//3)
            count+=1
        elif(n%5==0):
            n=4*(n//5)
            count+=1
        else:
            flag=0
            break
    print(count) if(flag) else print(-1)