import sys

input = sys.stdin.readline
N, M = map(int, input().split())
ans = 0
C = [0] * M
S = [0] * N
A = list(map(int, input().split()))

S[0] = A[0]
# 합배열 구하기
for i in range(1, N):
    S[i] = S[i - 1] + A[i]

# S[i] - S[j] 의 뜻은 i-1 ~ j 까지의 합을 의미
# 이 나머지들의 차이가 0이면, 그 구간의 합은 0이라는 것을 의미
# 따라서 해당 나머지의 값들이 몇개인지를 찾아서 2개를 선택하는 조합으로 추가해줘야함
for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        # 나머지의 합이 0인 개수들은 1 인덱스부터 해당 구간까지 구간합이 0 이므로 먼저 카운팅
        ans += 1

    C[remainder] += 1

# 나머지들의 차가 0이라는 점을 이용해 같은 합배열의 나머지값들이 같은 것중 2개를 선택하는 조합으로 카운팅
for i in range(M):
    if C[i] > 1:
        comb = (C[i] * (C[i] - 1)) // 2
        ans += comb

print(ans)
