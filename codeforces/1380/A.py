for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    for i in range(n-2):
        if lis[i]<lis[i+1]>lis[i+2]:
            print("Yes")
            print(i+1,i+2,i+3)
            break
    else:
        print("No")