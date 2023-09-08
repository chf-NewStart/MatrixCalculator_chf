from uti import confirmation, createMatrix, prompt
from affordancesScript import matrix_insp, matrix_multi


def affordances(some_matrix_in, some_option):

    if some_option == "quit":
        return
    elif some_option == "1":
        return matrix_insp(some_matrix_in)
        
    elif some_option == "2":
        some_matrix_in2 = createMatrix()
        return matrix_multi(some_matrix_in,some_matrix_in2)

"""    
    elif some_option == "2":
        return other_func(some_matrix_in)
"""


def mainfunc():
    matrix_in = createMatrix()
    option = prompt()

    while option != "quit":
        #confirmation
        option = confirmation(option)
        
        #do what the user asked and confirmed
        affordances(matrix_in, option)

        # remodify option if needed
        option = prompt()

    return



mainfunc()



