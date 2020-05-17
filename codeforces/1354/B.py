for _ in range(int(input())):
    s=input()
    first=s[0]
    length=1
    second=''
    best=2000000
    for i in range(1,len(s)):
        if(s[i]!=first and second==''):
            second=s[i]
            length+=1
        elif(s[i]==first and second!=''):
            first,second=second,first
            length=2
        elif(s[i]==second):
            length+=1
        elif(s[i]!=first and s[i]!=second):
            length+=1
            best=min(best,length)
            first,second=second,s[i]
            length=2
    print(best) if(best!=2000000) else print(0)