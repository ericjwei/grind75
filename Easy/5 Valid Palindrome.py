import re
def isPalindrome(s: str) -> bool:
    s = re.sub(r'[\W_]+', '', s).lower()
    return s == s[::-1]

s = "helloolleh"
print(isPalindrome(s))
