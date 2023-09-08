import numpy as np
from numpy.linalg import matrix_rank



def matrix_insp(some_matrix_in):

    shape_of_matrix = some_matrix_in.shape
    rank_of_matrix = matrix_rank(some_matrix_in)
    m = shape_of_matrix[0]
    if rank_of_matrix == m:
        isLinearindep = True
    elif rank_of_matrix<m:
        isLinearindep = False
    

    print("\n-----------------matrix_insp-----------------")
    print("The matrix is: \n", some_matrix_in)
    print("The shape of the matrix is: ",shape_of_matrix)
    print("The rank of your matrix is: ", rank_of_matrix)
    print("isLinearindep: ", isLinearindep)
    print("-----------------matrix_insp-----------------\n")


    return


def matrix_multi(A,B):
    # A shape (m,n)
    # B shape (n,p)
    A_shape = A.shape
    B_shape = B.shape
    

    finalProduct_ls = np.zeros((A_shape[0],B_shape[-1]))

    if A_shape[-1] == B_shape[0]:
        # then we can perform matrix multi
        for i in range(0,A_shape[0]):
            for j in range(0,B_shape[-1]):
                for k in range(0,A_shape[-1]):
                    """
                    print("---debug---")
                    print("k: \n", k)
                    print("A[i][k]: \n",A[i][k])
                    print("B[k][j]: \n",B[k][j])
                    print("---debug---")
                    """
                    finalProduct_ls[i][j] = finalProduct_ls[i][j]+ A[i][k]*B[k][j]
    
    print("\n-----------------matrix_multi-----------------")
    print("Matrix A is: \n", A)
    print("Matrix B is: \n", B)
    print("The finalProduct matrix is: \n", finalProduct_ls)
    print("-----------------matrix_multi-----------------\n")

    return


    #else:
        # it's wrong! try another matrix

    
