def isAnagram(s: str, t: str) -> bool:
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for j in t:
        if j in dict:
            dict[j] -= 1
            if dict[j] == 0:
                dict.pop(j)
        else:
            return False
    return len(dict) == 0

s = "anagrammm"
t = "anagrammm"
print(isAnagram(s, t))