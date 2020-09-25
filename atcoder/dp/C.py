from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
n = int(input())
a = []
for i in range(n):
    tmp = list(map(int,input().split()))
    a.append(tmp)
dp = {}

@bootstrap
def DP(day, flag):
    key = (day,flag)
    if day == n:
        yield 0

    if key in dp:
        yield dp[key]
    
    ans = 0
    tmp1 = yield DP(day+1,1)
    tmp2 = yield DP(day+1,2)
    tmp3 = yield DP(day+1,3)
    if flag == 0:
        ans = max(ans, a[day][0] + tmp1)
        ans = max(ans, a[day][1] + tmp2)
        ans = max(ans, a[day][2] + tmp3)
    elif flag == 1:
        ans = max(ans, a[day][1] + tmp2)
        ans = max(ans, a[day][2] + tmp3)
    elif flag==2:
        ans = max(ans, a[day][0] + tmp1)
        ans = max(ans, a[day][2] + tmp3)
    else:
        ans = max(ans, a[day][0] + tmp1)
        ans = max(ans, a[day][1] + tmp2)
    dp[key] = ans
    yield ans
print(DP(0,0))