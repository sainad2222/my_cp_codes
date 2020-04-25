for _ in range(int(input())):
    n  = int(input())
    lis = list(map(int,input().split()))
    odd,even = 0,0
    for i in lis:
        if(even >=1 and odd>=1):
            break
        if(i&1==0):
            even+=1
        else:
            odd+=1
    if(odd&1!=0 or (even>=1 and odd>=1)):
        print("YES")
    else:
        print("NO")