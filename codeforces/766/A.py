a = input()
b = input()
ans=0
if(a == b):
    ans=-1
else:
    ans = max(len(a),len(b))
print(ans)