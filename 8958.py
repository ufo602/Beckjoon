N = int(input())
result = [];

for i in range(N):
    a = input()
    total = 0
    x = 0
    score = 0
    while True:
        if x == len(a):
            break
        #print(len(a))
        #print(score, total, a[x])
        if a[x] == 'O':
            score += 1
            total += score
        else:
            score = 0
        x += 1


    print(total)
