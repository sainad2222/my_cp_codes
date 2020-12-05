# First code from nvim
for _ in range(int(input())):
    n,m = map(int,input().split())
    bot = list(map(int,input().split()))
    left = list(map(int,input().split()))
    left = set(left)
    ans = 0
    for i in bot:
        if i in left:
            ans+=1
    print(ans)
