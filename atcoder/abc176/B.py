n = input()
su = 0
for i in n:
    su += int(i)
print("Yes") if su%9==0 else print("No")