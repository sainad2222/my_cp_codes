n,k=map(int,input().split())
inp = list(map(int,input().split()))
count=0
for i in inp:
    if(i>0 and i>=inp[k-1]):
        count+=1
print(count)