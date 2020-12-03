lis = list(map(int,input().split()))
lis.sort()
ab,bc,ac,abc = lis
a = -abc+(ab+bc)
b = -abc+(ab+ac)
c = -abc+(ac+bc)
print(a,b,c)
