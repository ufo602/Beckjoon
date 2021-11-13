import os
x = 1; y =1
i = -1
c = []
while x!=0 and y !=0:
    x, y = map(int, os.sys.stdin.readline().split())
    c.append(x+y)
    i += 1
for n in range(i):
    print(c[n])