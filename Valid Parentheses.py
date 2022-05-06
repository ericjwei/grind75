def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == ")" or i == "}" or i == "]":
            if i == stack[-1]:
                stack.pop()
        elif i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        else:
            stack.append("]")

    return len(stack) == 0

s = "({[]()}[])"
print(isValid(s))
