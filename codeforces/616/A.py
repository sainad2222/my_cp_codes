a = input()
b = input()
acount,bcount = 0,0
for i in a:
    if i == '0':
        acount += 1
    else:
        break
for i in b:
    if i == '0':
        bcount += 1
    else:
        break
a = a.replace('0','',acount)
b = b.replace('0','',bcount)
if len(a) == len(b):
    for i, j in zip(a, b):
        if i > j:
            print(">")
            exit()
        elif i < j:
            print("<")
            exit()
    print("=")
elif len(a) > len(b):
    print(">")
else:
    print("<")