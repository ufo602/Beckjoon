
a = []

while len(a) != 9:
    a.append(int(input()))

print(max(a))
print(a.index(max(a))+1)
