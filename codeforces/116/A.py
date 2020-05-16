n = int(input())
cap=0
msf = -1
for i in range(n):
    a,b=map(int,input().split())
    cap+=b-a
    msf = max(cap,msf)
print(msf)