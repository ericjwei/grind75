from urllib.response import addbase


def addBinary(a: str, b: str) -> str:
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    result = ""
    while i >= 0 or j >= 0 or carry > 0:
        carry += int(a[i]) if i >= 0 else 0
        carry += int(b[j]) if j >= 0 else 0
        result = str(carry % 2) + result
        carry //= 2
        i -= 1
        j -= 1
    return result 

a = "1010"
b = "1011"
print(addBinary(a, b))

