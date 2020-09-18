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
n, k = map(int, input().split())
lis = list(map(int, input().split()))
dp = {}
@bootstrap
def TD(idx):
    if idx==n-1:
        yield 0
    if idx in dp:
        yield dp[idx]
    mi = float('inf')
    for i in range(1, k + 1):
        if i+idx < n:
            tmpx = yield TD(idx+i)
            tmp = abs(lis[idx]-lis[i+idx])+tmpx
            mi = min(mi, tmp)
    dp[idx] = mi
    yield mi
print(TD(0))