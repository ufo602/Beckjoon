N = int(input())
sum = 0
count = 0
first_N = N

while True:

    if N < 10:
        X = N % 10
        Y = X
        #sum = X + Y
        N = int(str(Y) + str(X))
        #print(sum, N)
        count += 1

    else:
        X = N // 10
        Y = N % 10
        sum = X + Y
        N = int(str(Y) + str(sum % 10))
        #print(sum, N)
        count += 1

    if first_N == N:
        print(count)
        break









