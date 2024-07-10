s="basava"
s2="shiva"
l=[]
for i in range(len(s)-1):
    if s[i] not in s2:
        l.append(s[i])

print(l)
