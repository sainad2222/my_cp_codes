for _ in range(int(input())):
    n = int(input())
    x = int(pow(n, 0.5))
    # First we need to increase and then copy that number to get req
    # in min steps possible
    # suppose we increased to x
    # 1->x       steps = x-1
    # x+k*x=n    suppose we need k steps later
    # k = ((n+x-1)//x)-1     ceil of n/x-1
    # total ops = x-1+k
    # now bruteforce for x 
    # NTFS: x can be max of sqrt(n)

    ans = x - 1 + ((n + x - 1) // x) - 1
    print(ans)