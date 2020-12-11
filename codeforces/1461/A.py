for _ in range(int(input())):
    n,k = map(int,input().split())
    print('abc'*(n//3),end="")
    if n%3==0:
        print()
    elif n%3==1:
        print('a')
    else:
        print('ab')
