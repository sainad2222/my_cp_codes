for _ in range(int(input())):
    n = int(input())
    s = input()
    cur = 0
    for i in s[::-1]:
        if i==')':
            cur+=1
        else:
            break
    print("Yes") if cur>n//2 else print("No")
