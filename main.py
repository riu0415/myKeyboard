N,W = map(int,input().split())
dp = [[0]*(10**5+1) for i in range(N+1)]
Q = [list(map(int,input().split()))]
for i in range(1,N+1):
    w,v = map(int,input().split())
    for j in range(10**5+1):
        if j-v >= 0 and dp[i][j-v]-w < W:
            dp[i][j] = max(dp[i-1][j],dp[i][j-v]+w)
ans = 0
for i in range(10**5+1):
    if dp[-1][i]:
        ans = i
print(ans)