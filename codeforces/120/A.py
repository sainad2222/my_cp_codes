import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
door,rail = input(),input()
if((door=='front' and rail=='1') or (door=='back' and rail=='2')):
    ans="L"
else:
    ans="R"
print(ans)