X = []
a = []


a = [int(i) for i in input().split()]

for _ in range(a[0]):
    X.append([int(val) for val in input().split()])

multiplier = int(input())


result = X

for i in range(len(result)):
    # iterate through columns
    for j in range(len(result[0])):
        result[i][j] *= multiplier
for item in result:
    print(' '.join(str(x) for x in item))
