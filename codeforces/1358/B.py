for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    cur = 1
    lis.sort()
    i=0
    tmp=[]
    while(i<n):
        if(cur>=lis[i]):
            cur+=1
            i+=1
        else:
            tmp = lis[i:]
            break
    while(len(tmp)!=0):
        tempc = cur
        tempc+=len(tmp)-1
        if(tmp[-1]>tempc):
            tmp.pop()
        else:
            cur+=len(tmp)
            break
    print(cur)