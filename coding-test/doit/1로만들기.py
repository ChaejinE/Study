import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
if N >= 2:
    dp[2] = 1
    if N >= 3:
        dp[3] = 1

for i in range(4, N + 1):
    dp[i] = dp[i - 1]
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3])
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2])
    dp[i] += 1

print(dp[N])
