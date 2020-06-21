from collections import Counter
n = int(input())
lis = list(map(int,input().split()))
l = Counter(lis)
d = [0]+[l[i+1] for i in range(10**5)]
q = int(input())
s = sum(lis)
for i in range(q):
    a,b=map(int,input().split())
    if d[a]!=0:
        temp = d[a]
        d[a]=0
        d[b]+=temp
        s += temp*(b-a)
    print(s)