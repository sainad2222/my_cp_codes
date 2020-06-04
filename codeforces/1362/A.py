for _ in range(int(input())):
    a,b=map(int,input().split())
    count=0
    flag=1
    num = max(a,b)
    den = min(a,b)
    if(num%den!=0):
        print(-1)
        continue
    elif(num==den):
        print(0)
        continue
    else:
        val = num//den
        while(val!=1):
            if(val%8==0):
                val=val//8
                count+=1
            elif(val%4==0):
                val=val//4
                count+=1
            elif(val%2==0):
                val=val//2
                count+=1
            else:
                flag=0
                break
        
    if(flag==0):
        print(-1)
    else:
        print(count)