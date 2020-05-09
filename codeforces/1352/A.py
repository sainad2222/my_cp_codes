for _ in range(int(input())):
    n = int(input())
    length=0
    res=[]
    while(n>0):
        r = n%10
        n=n//10
        if(r!=0):
            res.append(str(r)+'0'*(length))
        length+=1
    print(len(res))
    print(' '.join(res))