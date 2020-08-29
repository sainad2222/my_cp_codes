d, t, s = map(int, input().split())
dist = 0
time = 0
while dist < d and time<=t:
    dist += s
    time += 1
if time > t:
    print("No")
else:
    print("Yes")