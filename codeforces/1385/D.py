# NTFS: Code NCode
def getCost(l,mid,ch):
    return mid-l+1-(s[l:mid+1].count(ch))
def getMin(l,r,ch):
    if l==r:
        if s[l]==ch:
            return 0
        else:
            return 1
    mid = (l+r)//2
    return min(getCost(l,mid,ch)+getMin(mid+1,r,chr(ord(ch)+1)),
    getCost(mid+1,r,ch)+getMin(l,mid,chr(ord(ch)+1))
    )
for _ in range(int(input())):
    n = int(input())
    s = input()
    print(getMin(0,n-1,'a'))