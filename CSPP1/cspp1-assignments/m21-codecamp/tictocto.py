def row_check(matrix):

    if matrix[0][0] == matrix[0][1] == matrix[0][2]:
        return matrix[0][0]
    if matrix[1][0] == matrix[1][1] == matrix[1][2]:
        return matrix[1][1]
    if matrix[2][0] == matrix[2][1] == matrix[2][2]:
        return matrix[2][0]

def col_check(matrix):

    if matrix[0][0] == matrix[0][1] == matrix[0][2]:
        return matrix[0][0]
    if matrix[0][1] == matrix[1][1] == matrix[2][1]:
        return matrix[1][1]
    if matrix[2][0] == matrix[2][1] == matrix[2][2]:
        return matrix[2][0]

def diagonal_check(matrix):

    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    if matrix[0][1] == matrix[1][1] == matrix[2][0]:
        return matrix[1][1]
def read_data():

    matrix = []
    # try:
    # except TypeError:
    #     print("Error: Invalid input for the matrix")
    # else:
    for _ in range(0, 3, 1):
        values = input()
        temp = values.split(" ")
        k = []
        for j in temp:
            k.append(j)
        matrix.append(k)
    return matrix
def check_ttt(matrix):
    for row in range(3):
        for column in range(3):
            if (matrix[row][column] != 'x' and matrix[row][column] != 'o'
                    and matrix[row][column] != '.'):
                return True
    return False
    element_x = 0
    element_o = 0
    element_dot = 0
    for inputs in matrix:
        for j in inputs:
            if j == 'x':
                element_x += 1
            elif j == 'o':
                element_o += 1
            elif j == '.':
                element_dot += 1
    if abs(element_x - element_o >= 2):
        return False
    elif abs(element_x - element_o == 0) and element_dot > 0:
        return False
    return True 
def winner_ttt(matrix):
    win = None
    win = row_check(matrix)
    if win == None:
        win = col_check(matrix)
    elif win == None:
        win = diagonal_check(matrix)
    elif win == None:
        print("draw")
    return win

def main():
    """ main function of the matrix-operation"""
    try:
    # read matrix
    	mx = read_data()
    except ValueError:
        print("Error: Invalid input for the matrix")
    else:
        won_xoroordot = winner_ttt(mx)
        print(won_xoroordot)

if __name__ == '__main__':
    main()
