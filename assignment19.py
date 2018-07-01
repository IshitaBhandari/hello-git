#ASSIGNMENT ON NUMPY:
#Question 1:Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.
import numpy as np
array=np.random.rand(10,1)
print("ELEMENTS:",array)
m=np.mean(array)
print("MEAN:",m)

#Question 2:Create a numpy array with 20 elements of the shape(20,1) using np.random and find the variance and standard deviation of the elements.
import numpy as np
array=np.random.rand(20,1)
print("ELEMENTS:",array)
variance=np.var(array)
print("VARIANCE:",variance)
standard=np.std(array)
print("STANDARD DEVIATION:",standard)

#Question 3:Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.
import numpy as np
A=np.random.rand(10,20)
B=np.random.rand(20,25)
print(type(A))
print(type(B))
#to compute the matrix multiplication of A and B.
matrixmul=np.dot(A,B)
print(matrixmul)
#to print shape of new matrix
print(matrixmul.shape)
#to find sum of all elements of matrix.
matrix=np.matrix(matrixmul)
print(matrix.sum())

#Question 4:Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A. Apply this function to each element of A and print the new array holding the value the function returns.
import numpy as np
import math
A=np.random.rand(10,1)
print("ORIGINAL ARRAY:",A)

for x in np.nditer(A,op_flags=['readwrite']):
    x[...]=1+(1+math.exp(-x))
print("NEW ARRAY",A)
print(A.shape)