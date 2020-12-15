for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    i = 0
    j = n-1
    od = True
    while i<=j:
        if od:
            print(lis[i],end=" ")
            i+=1
        else:
            print(lis[j],end=" ")
            j-=1
        od = not od
    print()

