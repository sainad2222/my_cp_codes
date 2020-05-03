s = input()
flag=0
for i in s:
    if(i=='H' or i=='Q' or i=="9"):
        flag=1
        break
print("YES") if(flag) else print("NO")