n = int(input())
if n<=2:
    print("No")
    exit()
print("Yes")
print(n//2,end=" ")
lis = [x for x in range(2,n+1,2)]
print(' '.join(map(str,lis)))
if n&1:
    print((n//2)+1,end=" ")
else:
    print(n//2,end=" ")
lis = [x for x in range(1,n+1,2)]
print(' '.join(map(str,lis)))