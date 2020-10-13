from collections import deque, defaultdict
n = int(input())
s = input()

dic = defaultdict(lambda: deque())
rev = s[::-1]
for i,char in enumerate(rev):
    dic[char].append(i + 1)
arr = []
for i in s:
    arr.append(dic[i].popleft())

class BIT:
    def __init__(self, lis, n):
        self.n = n
        self.array = [0] + lis
        for idx in range(1,n):
            idx2 = idx+(idx & -idx)
            if idx2 < n:
                self.array[idx2] += self.array[idx]
    
    def prefix_query(self,idx):
        idx+=1
        result = 0
        while idx > 0:
            result += self.array[idx]
            idx -= (idx & -idx)
        return result
    
    def range_query(self, from_idx, to_idx):
        return self.prefix_query(to_idx) - self.prefix_query(from_idx-1)
    
    def update(self,idx,add):
        idx+=1
        while idx<=self.n:
            self.array[idx]+=add
            idx += (idx & -idx)
        
        
    def __str__(self):
        return ' '.join(map(str,self.array))

n = len(arr)
ma = max(arr)
lis = [0] * (ma)
bit = BIT(lis, ma)
ans = 0
for i in range(n):
    # print(ma - 1, arr[i] - 1)
    ans += bit.range_query(ma, arr[i]-1)
    bit.update(arr[i] - 1, 1)
    # print(bit,"    ",ans)
print(abs(ans))