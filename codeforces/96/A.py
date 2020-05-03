s = input()
flag=1
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            if(j-i>=6):
                flag=0
                break
        else:
            break
print("YES") if flag==0 else print("NO")