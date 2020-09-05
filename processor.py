X = []
Y = []


a = []
b = []

a = [int(i) for i in input().split()]
for _ in range(a[0]):
    X.append([int(val) for val in input().split()])

b = [int(j) for j in input().split()]
for _ in range(b[0]):
    Y.append([int(x) for x in input().split()])

#line = [0] * a[1]
#for _ in range(a[0]):
#    result.append(line)
result = X
#print(result)

if a[0] != b[0] or a[1] != b[1]:
    print("ERROR")
else:
    for i in range(len(result)):
        # iterate through columns
        for j in range(len(result[0])):
            result[i][j] += Y[i][j]
    for item in result:
        print(' '.join(str(x) for x in item))
