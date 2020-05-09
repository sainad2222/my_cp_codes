for _ in range(int(input())):
    n,k=map(int,input().split())
    res=[]
    if((n%2!=0 and k%2==0) or (n<k)):
        res=[]
    else:
        if(n%k==0):
            res = [n//k for i in range(k)]
        elif((n%2!=0 and k%2!=0) or (n%2==0 and k%2==0)):
            res = [1 for i in range(k-1)]
            res.append(n-(k-1))
        else:
            res=[2 for i in range(k-1)]
            su = sum(res)
            if(n-su>0):
                res.append(n-su)
            else:
                res=[]
    if(len(res)==0):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str,res)))