# import sys
# sys.setrecursionlimit(10**6)
# n, a, b, c = map(int, input().split())
# wt = [a, b, c]
# dp = {}
# def knapsack(wt,C):
#     n = len(wt)
#     if C in dp:
#         return dp[C]
#     if C == 0:
#         return 0
#     ans = -1
#     for val in wt:
#         if val <= C:
#             ans = max(ans, 1 + knapsack(wt, C - val))
#     dp[C] = ans
#     return ans
# print(knapsack(wt,n))
import sys 
    
#As Python has recursion limit we extend the recusrion limit to avoid runtime error due to large number of recursive calls 
sys.setrecursionlimit(500000000) 
    
def f(n): 
    """ 
    returns maximum number of pieces that can be cut for ribbon with length n 
    """ 
        
    # If maximum num of pieces for length n is already computed simply return it 
    if n in memo.keys(): 
        return memo[n] 
    
    ans = float("-inf") 
    if n == 0: 
        return 0 
    for length in l: 
        # Cut into pieces if only we dont have negative length of ribbon 
        if n >= length: 
            ans = max(ans, 1 + f(n - length)) 
    #Cache the result 
    memo[n] = ans 
    return ans 
        
#Dict to store computed values 
memo = dict() 
    
l = list(map(int, input().split())) 
n, l = l[0], l[1:] 
print(f(n)) 