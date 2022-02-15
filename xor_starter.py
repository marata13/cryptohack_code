s = "label"
b = []
for i in range(len(s)):
    b.append(chr((ord(s[i]) ^ 13)))
c = "".join(b)
print(c)
