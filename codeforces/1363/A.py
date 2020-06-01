for _ in range(int(input())):
    n,x=map(int,input().split())
    lis = list(map(int,input().split()))
    odd = 0;even=0
    for i in lis:
        if(i&1):
            odd+=1
        else:
            even+=1
    if(odd==0):
        print("No")
    else:
        odd=min(odd,x)
        if(odd%2==0):
            odd-=1
        remain = x-min(x,odd)
        if(remain<=even):
            print("Yes")
        else:
            print("No")