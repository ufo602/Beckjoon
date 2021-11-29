a = []
i = 0; count = 0;
while len(a) != 10:
    a.append(int(input()) % 42)
    if a.count(a[i]) == 1:
        count += 1
    i +=1
print(count)
'''
for i in range(len(a)):
    if a.count(a[i]) == 1:
        count += 1
'''

