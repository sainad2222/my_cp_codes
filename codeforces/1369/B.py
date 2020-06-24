for _ in range(int(input())):
    n = int(input())
    s = input()
    zeros,ones = 0,0
    for i in s:
        if i=='0':
            zeros+=1
        else:
            break
    for i in reversed(range(n)):
        if s[i]=='1':
            ones+=1
        else:
            break
    print('0'*zeros,end="")
    if(zeros+ones!=n):
        print('0',end="")
    print('1'*ones)