def isBadVersion(version: int) -> bool:
    return version >= 14

def firstBadVersion(n: int) -> int:
    return firstBadVersionHelper(0, n)

def firstBadVersionHelper(lower: int, upper: int) -> int:
    check = (upper - lower) // 2 + lower
    curr = isBadVersion(check)
    prev = isBadVersion(check - 1)
    if curr and not prev:
        return check
    elif curr and prev:
        return firstBadVersionHelper(lower, check - 1)
    else:
        return firstBadVersionHelper(check + 1, upper)

print(firstBadVersion(20))


    