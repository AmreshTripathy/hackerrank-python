s = input()
p = ''
for i in s:
    if (i == i.upper()):
        p += i.lower()
    elif (i == i.lower()):
        p += i.upper()
print (p)
