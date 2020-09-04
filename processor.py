matrix_a = [[1, 2, 3, 4, 5], [3, 2, 3, 2, 1], [8, 0, 9, 9, 1], [1, 3, 4, 5, 6]]
matrix_b = [[1, 1, 4, 4, 5], [4, 4, 5, 7, 8], [1, 2, 3, 9 ,8], [1, 0, 0, 0, 1]]
matrix_out = []

a = [4, 5]
b = [4, 5]

#a = [int(i) for i in input().split()]
#for _ in range(a[0]):
 #   matrix_a.append([int(val) for val in input().split()])

#b = [int(j) for j in input().split()]
#for _ in range(b[0]):
 #   matrix_b.append([int(x) for x in input().split()])

line = [0] * a[1]
for _ in range(a[0]):
    matrix_out.append(line)
#print(matrix_a)
#print(matrix_b)
print(matrix_out)

if a[0] != b[0] or a[1] != b[1]:
    print("ERROR")
else:
    for i in range(a[0]):
        # iterate through columns
        for j in range(a[1]):
            matrix_out[i][j] = matrix_a[i][j] + matrix_b[i][j]
            print(matrix_out[i][j])
        print(matrix_out[i])

print(matrix_out)
for item in matrix_out:
        print(' '.join(str(x) for x in item))
