s = input()
cou = s.count("a")
if 2*cou-1>len(s):
    print(len(s))
else:
    print(2*cou-1)