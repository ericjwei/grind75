def longestPalindrome(s: str) -> int:
    dict = {}
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    count = 0
    single = False
    for k in dict:
        count += dict[k] // 2
        if not single and dict[k] % 2 == 1:
            single = True

    if single:
        return count * 2 + 1
    return count * 2

s = "aabbcccd"
print(longestPalindrome(s))
