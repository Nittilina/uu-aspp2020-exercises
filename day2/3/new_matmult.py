# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

@profile
def generate_xmat(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

@profile
def generate_ymat(N):
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

@profile
def alloc_mat(N):
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

@profile
def multmat(X, Y, result):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            #Matrix multiply
            result[i][j] = np.dot(X[i], Y[:,j])
#    return result

X = generate_xmat(N)
Y = generate_ymat(N)
result = alloc_mat(N)

np_X = np.array(X)
np_Y = np.array(Y)
np_result = np.array(result)

multmat(np_X, np_Y, np_result)
#for r in result:
#    print(r)


