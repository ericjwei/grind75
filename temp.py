import random
temp = bytes([random.randrange(0, 256) for _ in range(0, 16)])
# print(temp)
# print(bytes(temp))
# temp = bytes(temp)
print(temp)

t = bytearray(temp[1:])
t.append(temp[0])
print(bytes(t))