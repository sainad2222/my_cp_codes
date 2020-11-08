from collections import defaultdict
dic = defaultdict(int)
s = input()
su = 0
for i in s:
    su += int(i)
    dic[int(i) % 3] += 1
if su % 3 == 0:
    print(0)
else:
    # dic[1] = dic[1]%3
    # dic[2] = dic[2]%3
    # ans = abs(dic[1] - dic[2])
    # if ans == len(s):
    #     print(-1)
    # else:
    #     print(ans)
    k = len(s)
    if su%3==1:
        if dic[1]!=0:
            if k>1:
                print(1)
            else:
                print(-1)
        elif dic[2]>1:
            if k>2:
                print(2)
            else:
                print(-1)
        else:
            print(-1)
    else:
        if dic[2]!=0:
            if k>1:
                print(1)
            else:
                print(-1)
        elif dic[1]>1:
            if k>2:
                print(2)
            else:
                print(-1)
        else:
            print(-1)
