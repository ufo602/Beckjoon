N = int(input())
a = [ i for i in range(1, N+1)]
count = 0

for i in a:
    if (i // 10 == 0) or (i // 100 == 0):
        count += 1
    else:
        b = str(i)
        gap = int(b[1]) - int(b[0])
        c = 0
        for x in range(len(b)):
            try:
                if int(b[x]) + gap == int(b[x+1]):
                    c += 1
            except:
                continue

        if c == len(b)-1:
            count += 1
print(count)