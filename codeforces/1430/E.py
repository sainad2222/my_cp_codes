from collections import defaultdict,deque
n = int(input())
s = input()
# helper function
def mergesort(arr,n):
    # temp arr to store sorted array after every merge operation
    temp_arr = [0]*n
    return _mergeSort(arr,temp_arr,0,n-1)

# main function
def _mergeSort(arr,temp_arr,left,right):
    inv_count = 0
    if left<right:
        mid = (left+right)//2
        inv_count += _mergeSort(arr,temp_arr,left,mid)
        inv_count += _mergeSort(arr,temp_arr,mid+1,right)
        inv_count += merge(arr,temp_arr,left,mid,right)
    return inv_count

# merge function
def merge(arr,temp_arr,left,mid,right):
    i = left
    j = mid+1
    k = left
    inv_count = 0

    while i<=mid and j<=right:
        # no inversion case
        if arr[i]<=arr[j]:
            temp_arr[k] = arr[i]
            k+=1
            i+=1
        # inversion case
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i+1)
            k+=1
            j+=1
    
    # copying remaining elements if any left
    while i<=mid:
        temp_arr[k] = arr[i]
        k+=1
        i+=1
    while j<=right:
        temp_arr[k] = arr[j]
        k+=1
        j+=1
    
    # copying the sorted subarray into original array
    for i in range(left,right+1):
        arr[i] = temp_arr[i]
    
    return inv_count

dic = defaultdict(lambda: deque())
rev = s[::-1]
for i,char in enumerate(rev):
    dic[char].append(i + 1)
arr = []
for i in s:
    arr.append(dic[i].popleft())
n = len(arr)
print(mergesort(arr,n))