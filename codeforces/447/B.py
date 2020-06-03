from string import ascii_lowercase as lower
s=input()
k = int(input())
lis = list(map(int,input().split()))
x={}
for i,j in zip(lower,lis):
    x[i]=j
val=0
nxt=1
for i in s:
    val+=nxt*x[i]
    nxt+=1
ma = max(x,key=x.get)
res = [x for x in range(len(s)+1,len(s)+k+1)]
for i in res:
    val+=i*x[ma]
print(val)