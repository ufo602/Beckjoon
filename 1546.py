N = int(input())
total = 0
a = list(map(int, input().split()))
bo = max(a)
for i in range(len(a)):
    total += a[i]/bo

print(total/N*100)
