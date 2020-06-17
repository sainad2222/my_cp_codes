for _ in range(int(input())):
    n,k=map(int,input().split())
    s = input()
    count = 0
    if '1' not in s:
        print(1+(len(s)-1)//(k+1))
        continue
    res = s.split('1')
    for i in range(1,len(res)-1):
        tmp = len(res[i])-2*k
        count += 1+(tmp-1)//(k+1)
    if len(res)>=2:
        tmp = len(res[0])-k
        count += 1+(tmp-1)//(k+1)
        tmp = len(res[-1])-k
        count += 1+(tmp-1)//(k+1)
        print(count)
    else:
        tmp = len(res[0])-k
        count += 1+(tmp-1)//(k+1)
        print(count)