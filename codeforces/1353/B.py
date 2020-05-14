for _ in range(int(input())):
    n,k=map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    for i in range(k):
        if(i>n-1):
            break
        if(A[i]<B[n-1-i]):
            A[i],B[n-1-i]=B[n-1-i],A[i]
    print(sum(A))