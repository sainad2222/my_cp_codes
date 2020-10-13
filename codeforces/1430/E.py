from collections import defaultdict,deque
n = int(input())
s = input()

def mergesort(arr, n):
    temp_arr = [0] * n
    return _mergesort(arr, temp_arr, 0, n - 1)

def _mergesort(arr, temp, l, r):
    ans = 0
    if l < r:
        mid = (l + r) // 2
        ans += _mergesort(arr, temp, l, mid)
        ans += _mergesort(arr, temp, mid + 1, r)
        ans += merge(arr, temp, l, mid, r)
    return ans

def merge(arr, temp, l, mid, r):
    count = 0
    i = l
    j = mid + 1
    nxt = l
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp[nxt] = arr[i]
            nxt += 1
            i += 1
        else:
            count += (mid - i + 1)
            temp[nxt] = arr[j]
            nxt += 1
            j += 1
    
    while i <= mid:
        temp[nxt] = arr[i]
        nxt += 1
        i += 1
    
    while j <= r:
        temp[nxt] = arr[j]
        nxt += 1
        j += 1
    
    arr[l:r+1] = temp[l:r+1][:]
    
    return count

dic = defaultdict(lambda: deque())
rev = s[::-1]
for i,char in enumerate(rev):
    dic[char].append(i + 1)
arr = []
for i in s:
    arr.append(dic[i].popleft())
n = len(arr)
print(mergesort(arr,n))