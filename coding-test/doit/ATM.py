import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
S = [0] * N

# point : greedy, and O(N^2) Sort => insert Sorting
for i in range(1, N):
    will_insert_value = P[i]

    # search min value
    will_insert_idx = i
    for j in range(i):
        if P[i] < P[j]:
            will_insert_idx = j
            break

    # shift
    for k in range(i, will_insert_idx, -1):
        P[k] = P[k - 1]

    # insert
    P[will_insert_idx] = will_insert_value

S[0] = P[0]
result = P[0]
for i in range(1, N):
    S[i] = S[i - 1] + P[i]
    result += S[i]

print(result)
