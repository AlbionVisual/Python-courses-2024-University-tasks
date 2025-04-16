from sys import argv as entries
# from time import time

def is_sub(sub, word):                      # Проверяет подпоследовательность ли sub для word
    m, n = len(sub), len(word)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    for j in range(n + 1): dp[0][j] = True
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):                   # dp[i][j] будет истинным, если первые i символов sub являются подпоследовательностью первых j символов word
            if sub[i - 1] == word[j - 1]: dp[i][j] = dp[i - 1][j - 1]
            else: dp[i][j] = dp[i][j - 1]
    
    return dp[m][n]


# start_time = time()
with open(entries[1], 'r') as file:
    words = file.read().splitlines()

result = [word for word in words if is_sub(entries[2], word)]

print(len(result), result)
# print(time() - start_time)