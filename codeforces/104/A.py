dic = {1:4,11:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:15}
n = int(input())
if n<=10 or n>=22:
    print(0)
    exit()
print(dic[n-10])