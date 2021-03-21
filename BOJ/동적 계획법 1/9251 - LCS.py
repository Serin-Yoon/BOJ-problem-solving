import sys

input = sys.stdin.readline

word1 = list(input())[:-1]
word2 = list(input())[:-1]

dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len(word1) - 1][len(word2) - 1])