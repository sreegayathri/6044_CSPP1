def mult_matrix(m1, m2):
    '''
        check if the matx1 columns = matx2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1[0]) != len(m2) and len(m1) != len(m2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    multiply = []
    for i in range(len(m1)):
        temp_mul = []
        for j in range(len(m2[0])):
            res = 0
            for k in range(len(m1[0])):
                res += m1[i][k]*m2[k][j]
            temp_mul.append(res)
        multiply.append(temp_mul)
    return multiply

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) != len(m2) & len(m1[0]) != len(m2[0]):
        print("Error: Matrix shapes invalid for addition")
        return None
    add1 = []
    for i in range(len(m1)):
        temp_sum = []
        for j in range(len(m1[0])):
            sum_matrix = m1[i][j] + m2[i][j]
            temp_sum.append(sum_matrix)
        add1.append(temp_sum)
    return add1

    #return add_matrix

            
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    try:
        dim = input().split(',')
    except:
        print("Error: Invalid input for the matrix")
    else:
        for i in range(0, int(dim[0]), 1):
            values = input()
            temp = values.split(" ")
            k = []
            for j in temp:
                k.append(int(j))
            matrix.append(k)
    # print(m1)
    # dim2 =input().split(',')
    # for i in range(0, int(dim2[0]),1):
    #     elements = input()
    #     temp2 = elements.split(" ")
    #     m = []
    #     for j in temp2:
    #         m.append(int(j))
    #     m2.append(m)
    # print(m2)
    return matrix

def main():
    try:
    # read matrix 1
        mx1 = read_matrix()
    # read matrix 2
        mx2 = read_matrix()
    except:
        print("Error: Invalid input for the matrix")
    else:
    # add matrix 1 and matrix 2
        addtion_x = add_matrix(mx1, mx2)
        print(addtion_x)
    # multiply matrix 1 and matrix 2
        multiply_matrix = mult_matrix(mx1, mx2)
        print(multiply_matrix)

if __name__ == '__main__':
    main()
