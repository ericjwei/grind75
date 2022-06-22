def canConstruct(ransomeNote: str, magazine: str) -> bool:
    dict = {}
    for c in magazine:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    for c in ransomeNote:
        if c in dict:
            dict[c] -= 1
            if dict[c] == 0:
                dict.pop(c)
        else: 
            return False
    return True
    
print(canConstruct('aaac', "aaba"))