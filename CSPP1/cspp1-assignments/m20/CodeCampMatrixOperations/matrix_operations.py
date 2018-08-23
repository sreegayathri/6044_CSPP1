def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if matrix1[i][j] == matrix2[i][j]:
        result_matrix1 = matrix1[i][j] * matrix2[j][i] 
    return result_matrix
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if matrix1[i][j] == matrix2[i][j]:
        result_matrix2 = matrix1[i][j] + matrix2[i][j] 
    return result_matrix
    

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    row_matrix = int(input("Enter a number: "))
    column _matrix = int(input("Enter a number: ")) 

def main():
    # read matrix 1
    matrix1 = read_matrix()
    # read matrix 2
    matrix2 = read_matrix()

    # add matrix 1 and matrix 2
    add_matrix = add_matrix(matrix1, matrix2)
    # multiply matrix 1 and matrix 2
    multiply_matrix = mult_matrix(matrix1, matrix2)

if __name__ == '__main__':
    main()
