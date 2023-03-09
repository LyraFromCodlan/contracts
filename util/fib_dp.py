# with list and recursion. Can compute 9968th fibonacci's number

def fib(n,dp) -> int:
    if dp[n]==-1:
        dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]

n =int(input())
dp =[-1]*(n+1)
dp[0]=dp[1]=1
print(fib(n,dp))

# with while. Can compute 10^5 fibonacci's number

n =int(input())
dp =[-1]*(n+1)
dp[0]=dp[1]=1
for ind in range(2,n+1):
    dp[ind]=dp[ind-1]+dp[ind-2]
print(dp[n])

# with only 2 variables. Can compute 10^6 fibonacci's number

n= int(input())
dp=[0,1]
for ind in range(2,n):
    dp[0],dp[1] = dp[1],dp[0]+dp[1]
print(dp[1])