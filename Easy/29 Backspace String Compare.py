def backspaceCompare(s: str, t: str) -> bool:
    return backSpaceCompareHelper(s) == backSpaceCompareHelper(t)

def backSpaceCompareHelper(s) -> str:
    i = 0
    while i < len(s):
        if s[i] == '#':
            if i == 0:
                s = s[1:]
            else:
                s = s[:i - 1] + s[i + 1:]
                i -= 1
        else:
            i += 1
    return s

s = 'ca#b#'
print(backspaceCompare(s, 'c'))
