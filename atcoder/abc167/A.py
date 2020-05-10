s = input()
t = input()
flag=0
if s in t:
  if(len(t)-len(s)==1 and s[0]==t[0]):
    flag=1
print("Yes") if(flag) else print("No")