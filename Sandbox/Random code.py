# Given two non-empty strings, write a function 'longest_common_substring(a, b)' that gives back an integer which indicates the length of the longest common substring between these two strings. For example:

# longest_common_substring('abcf','abcd') returns 3
# longest_common_substring('nghiiiii','nghiabdre') returns 4
# longest_common_substring('hehehihiheheho','hehebabaheheho') returns 6 

def longest_common_substring(a, b):
    max_length = 0
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)] # dp stands for dynamic programming
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
    return max_length