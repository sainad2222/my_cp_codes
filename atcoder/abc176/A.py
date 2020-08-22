n,x,t=map(int,input().split())
count = 0
time = 0
while count < n:
    count += x
    time += t
print(time)