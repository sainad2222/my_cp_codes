for _ in range(int(input())):
    a,b = map(int,input().split())
    count=0
    while(a!=b):
        if(a<b):
            x=abs(a-b)
            if(x&1!=0):
                a = a+x
                count+=1

            else:
                a=a+x-1
                count+=1

        else:
            y=abs(a-b)
            if(y&1==0):
                a=a-y
                count+=1

            else:
                a=a-y-1
                count+=1
    print(count)
    