for _ in range(int(input())):
    s = input()
    zeros = s.count('0')
    ones = s.count('1')
    count = 0
    while zeros>0 and ones>0:
        zeros-=1 
        ones-=1
        count+=1
    print("DA") if count&1 else print("NET")