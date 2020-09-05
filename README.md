# Numeric Matrix Processor

## Stage 1/6: Addition
Matrices have a wide range of applications in programming: they're used for digital image processing, graph representation and algorithms on a graph, graphic effects, applied math, statistics, and much more.

Since matrices are tables of numbers, they are usually presented in code as 2D-arrays. In this project, you will learn how to read and output matrices, do operations on them, and compute the determinant of a square matrix. At first, you will work with matrices with integer elements, and later the elements will be floating-point numbers.

### Description
Let’s start with matrix addition.

For two matrices to be added, they must have an equal number of rows and columns. The sum of matrices A and B will be a matrix with the same number of rows and columns as A or B. The sum of A and B, denoted A+B or B+A, is computed by adding the corresponding elements of A and B: (A+B)<sub>n,m</sub> = A<sub>n,m</sub> + B<sub>n,m</sub>. Notice that n in the index n,m represents the row and m represents the column.

Here is a simple example with numbers:

![matrices](https://i.imgur.com/qJ4DqRV.png)
### Objectives
In this stage, you should write a program that:

Reads matrix A from the input.
Reads matrix B from the input.
Outputs their sum if it is possible to add them. Otherwise, it should output the ERROR message.
Each matrix in the input is given in the following way: the first line contains the number of rows n and the number of columns m. Then n lines follow, each containing m integers representing one row of the matrix.

Output the result in the same way but don't print the dimensions of the matrix.

### Examples
#### Example 1:

Input:

4 5

1 2 3 4 5

3 2 3 2 1

8 0 9 9 1

1 3 4 5 6

4 5

1 1 4 4 5

4 4 5 7 8

1 2 3 9 8

1 0 0 0 1

Output:

2 3 7 8 10

7 6 8 9 9

9 2 12 18 9

2 3 4 5 7

#### Example 2:

Input:
```
2 3

1 4 5

4 5 5

4 5

0 1 0 4 5

1 7 8 9 4

1 2 3 5 6

1 3 4 3 8
```
Output:
```
ERROR
```

## Stage 2/6: Multiplication by number
### Description
In this stage, you are going to implement the multiplication of a matrix by a constant. To do this, you need to multiply every element of the matrix by that constant. You can see the example below:

![multiplication by number](https://i.imgur.com/dpf5XBs.png)
### Objectives
Write a program that reads a matrix and a constant and outputs the result of their multiplication.

The first line of the input contains the number of rows and the number of columns of the matrix. Next lines contain rows of the matrix. The last line contains the constant.

The constant and the elements of the matrix are integers.

### Examples
#### Example 1:

Input:
```
3 3
1 2 3
4 5 6
7 8 9
3
```
Output:
```
3 6 9
12 15 18
21 24 27
```
#### Example 2:

Input:
```
2 3
1 2 3
4 5 6
0
```
Output:
```
0 0 0
0 0 0
```

## Stage 3/6: Matrix by matrix multiplication
### Description
The next stage is the multiplication of matrices. This operation is a little more complex because it’s not enough to simply multiply the corresponding elements.

Unlike with addition, the sizes of the matrices can be different: the only restriction is that the number of columns in the first matrix equal the number of rows for the second matrix. Check out a comprehensive video by 3Blue1Brown about matrix multiplication.

The multiplication of A matrix with n rows and m columns and B matrix with m rows and k columns is Cn,k=An,m×Bm,k.

The resulting matrix has n rows and k columns, where every element is a sum of the multiplication of m elements across the rows of matrix A by m elements down the columns of matrix B.

Another really important thing is that A<sub>i,j</sub>×B<sub>j,k</sub> is not equal to Bj,k×Ai,j. In fact, these are not even possible to multiply if k≠i. If k=i, the resulting matrices would still be different.

Take a look at this example of matrix multiplication:

![matrix multiplication](https://i.imgur.com/4igFhXE.png)

### Objectives
In this stage, you should write a program that can do all operations on matrices that you've learned.

Write a program that does the following:

1. Prints a menu consisting of 4 options. The example shows what the menu should look like.
2. Reads the user's choice.
3. Reads all data (matrices, constants) needed to perform the chosen operation. The example shows the input format in each case.
4. Calculates the result and outputs it. The example shows how your output should look like.
5. Repeats all these steps.

The program should keep repeating this until the "Exit" option is chosen.

If some operation cannot be performed, output a warning message.

Also, you should support floating-point numbers.

#### Example

```
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 1
Enter size of first matrix: > 4 5
Enter first matrix:
> 1 2 3 4 5
> 3 2 3 2 1
> 8 0 9 9 1
> 1 3 4 5 6
Enter size of second matrix: > 4 5
Enter second matrix:
> 1 1 4 4 5
> 4 4 5 7 8
> 1 2 3 9 8
> 1 0 0 0 1
The result is:
2 3 7 8 10
7 6 8 9 9
9 2 12 18 9
2 3 4 5 7

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 2
Enter size of matrix: > 2 2
Enter matrix:
> 1.5 7.0
> 6.0 5.0
Enter constant: > 0.5
The result is:
0.75 3.5
3.0 2.5

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 3
Enter size of first matrix: > 3 3
Enter first matrix:
> 1 7 7
> 6 6 4
> 4 2 1
Enter size of second matrix: > 3 3
Enter second matrix:
> 3 2 4
> 5 5 9
> 8 0 10
The result is:
94 37 137
80 42 118
30 18 44

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 1
Enter size of first matrix: > 2 2
Enter first matrix:
> 1 2
> 3 2
Enter size of second matrix: > 1 1
Enter second matrix:
> 1
The operation cannot be performed.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 0
```