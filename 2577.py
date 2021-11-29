a = []
result = [0,0,0,0,0,0,0,0,0,0]

while len(a) != 3:
    a.append(int(input()))

sum = str(a[0] * a[1] * a[2])
for i in range(len(sum)):
    if sum[i] == '0':
        result[0] += 1
    elif sum[i] =='1':
        result[1] += 1
    elif sum[i] =='2':
        result[2] += 1
    elif sum[i] =='3':
        result[3] += 1
    elif sum[i] =='4':
        result[4] += 1
    elif sum[i] =='5':
        result[5] += 1
    elif sum[i] =='6':
        result[6] += 1
    elif sum[i] =='7':
        result[7] += 1
    elif sum[i] =='8':
        result[8] += 1
    elif sum[i] =='9':
        result[9] += 1

for i in range(10):
    print(result[i])