# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/ea83323a56db46b39caaa2132aed91af
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
blocks = [0 if s == 'B' else (1 if s == 'O' else 2) for s in (input())]
inf = float('inf')
dp = [[inf] * N for _ in range(N)]
dp[0][0] = 0

for i in range(N):
    for j in range(N):
        if j >= i:
            dp[i][j] = dp[i - 1][j]
        if i == 0:
            if (blocks[i] + 1) % 3 == blocks[j]:
                dp[i][j] = (j - i) ** 2
        else:
            if (blocks[i] + 1) % 3 == blocks[j]:
                if dp[i][j] > dp[i - 1][i] + (j - i) ** 2:
                    dp[i][j] = dp[i - 1][i] + (j - i) ** 2
            else:
                dp[i][j] = dp[i - 1][j]
print(-1 if dp[N - 1][N - 1] == inf else dp[N - 1][N - 1])