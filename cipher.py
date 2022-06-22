def encrypt(text: str, s: int) -> str:
    result = ""
    for c in text:
        if c.isspace():
            result += " "
        elif c.isupper():
            result += chr((ord(c) - 65 + s) % 26 + 65)
        else:
            result += chr((ord(c) - 97 + s) % 26 + 97)
    return result

def crack(text: str) -> str:
    for i in range(26):
        print(encrypt(text, i))

# text = "This is a Cipherz"
# s = 4
# text = encrypt(text, s)
# # text = encrypt(text, -s)
# ?crack(text)

def transposition(text: str, column: int) -> str:
    result = ""
    for start in range(column):
        for i in range(start,len(text),column):
            result += text[i]
    return result

text = "helloworld!?"
column = 4
print(transposition(text, column))
