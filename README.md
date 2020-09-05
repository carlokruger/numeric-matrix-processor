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