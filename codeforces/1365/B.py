for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b = ''.join(map(str,b))
    slis=sorted(a)
    if(slis==a):
        print("Yes")
        continue
    if '0' in b and '1' in b:
        print("Yes")
    else:
        print("No")