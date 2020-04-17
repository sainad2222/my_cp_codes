for _ in range(int(input())):
    n = int(input());flag=0
    lis = list(map(int,input().split()))
    lis.sort()
    for i in range(len(lis)-1):
        if(lis[i+1]==lis[i]+1):
            flag = 1
    if(flag==1):
        print(2)
    else:
        print(1)
            
