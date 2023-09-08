import numpy as np
import re


exlaimstr = """what else do you want to do? 
           [1]:-> matrix inspection;
           [2]:-> matrix calculation;
           [3]:-> matrix manipulation;
           [quit]:-> exit this program"""


def exlaim(astring):
    print(astring)

    

def confirmation(some_option):

    if some_option == "quit":
        conf = input("confirm to quit by pressing enter, to stay enter any other key...")
        if conf == "":
            return
        else:
            exlaim(exlaimstr)
            new_option = input("your option is ?...: ")
            some_option = new_option

    else:
        if some_option == "1":
            conf = input("confirm to run a matrix inspection?  enter to confirm, if not enter any other key")
            if conf == "":
                return some_option
            else:
                exlaim(exlaimstr)
                new_option = input("your option is ?...: ")
                some_option = new_option
    
    return some_option

def createMatrix(): # i first split it to 2 halfs (input + reshape), but later figured maybe i should put them together for easier calls
    # input string

    str_in = input("whats the values of ur matrix, start from left to right, then up to down: ")

    # what if the user made a mistake in one of his input, try to pick it up and make the user to change it, sub it back...

    cleared_str_in = re.sub('[^-0-9]',' ',str_in)

    space_splited_str_in = cleared_str_in.split()

    num_ls = []

    for index in range(0,len(space_splited_str_in)):
        num_ls.append(float(space_splited_str_in[index]))

    # for debugging:::
    print(str_in)
    print(cleared_str_in)
    print(num_ls)

    # describe m and n 
    exlaim("what shape do you want your matrix to be, m by n, m being the number of row, n being the number of col: ")

    # now we have the input, reshape into a matrix
    m = int(input("m (num of rows): "))
    n = int(input("n (num of cols): "))

    matrix = np.array(num_ls).reshape(m,n)

    print(matrix)
    return matrix


def prompt():

    exlaim(exlaimstr)
    
    user_option = input("your option is ?...: ")

    return user_option


