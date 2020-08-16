# NTFS secondthreadYT
# trick is starting from decreasing point go upto end and add 1 to rest of the elements
# This way diff wouldn't change among the next elements since we are adding to all of them
for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    ans = 0
    for i in range(1,n):
        if lis[i] < lis[i - 1]:
            ans += (lis[i - 1] - lis[i])
    print(ans)