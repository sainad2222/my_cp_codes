for _ in range(int(input())):
    n = int(input())
    sum =1 
    for i in range(2,n+1):
        sum += pow(2,i-1)
        if(n%sum==0):
            print(n//sum)
            break