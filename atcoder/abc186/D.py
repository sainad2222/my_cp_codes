def sumPairs(arr, n): 
    sum = 0
    for i in range(n - 1, -1, -1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

n = int(input())
lis = list(map(int,input().split()))
lis.sort()
print(sumPairs(lis,n))
