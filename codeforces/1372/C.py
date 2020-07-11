for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    arr = [0]*n
    for i in range(n):
        if lis[i]==i+1:
            arr[i]=1
    s = ''.join(map(str,arr))
    if '0' not in s:
        print(0)
        continue
    res = s.split('1')
    cou = 0
    for i in res:
        if len(i)>0:
            cou+=1
    if cou>1:
        print(2)
    else:
        print(1)