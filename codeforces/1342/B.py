for _ in range(int(input())):
    s = input()
    x = set(s)
    count=0
    for i in x:
        count+=1
    if(count==1):
        print(s)
    else:
        if(s[0]=="0"):
            print("01"*len(s))
        else:
            print("10"*len(s))
