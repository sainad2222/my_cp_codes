s = input()
st=''
for i in s:
    if(i=='h' and st==''):
        st+=i
    elif(i=='e' and st=='h'):
        st+=i
    elif(i=='l' and (st=='he' or st=='hel')):
        st+=i
    elif(i=='o' and st=='hell'):
        st+=i
print("YES") if(st=='hello') else print("NO")