N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    standard_line = sum(a[1:]) / a[0]
    count = 0
    for x in a[1:]:
        if x > standard_line:
            count += 1
    print("{0:.3f}%".format(count/a[0]*100))


