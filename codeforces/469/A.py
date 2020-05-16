n = int(input())
lisp = list(map(int,input().split()))[1:]
lisq = list(map(int,input().split()))[1:]
res = [0]*n
for i in lisp:
    if(i==0):
        break
    res[i-1]=1
for i in lisq:
    if(i==0):
        break
    res[i-1]=1
flag=1
for i in res:
    if(i==0):
        flag=0
print("I become the guy.") if(flag==1) else print('Oh, my keyboard!')