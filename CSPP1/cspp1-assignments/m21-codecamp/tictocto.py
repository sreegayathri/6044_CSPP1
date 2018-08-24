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
    if matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[1][1]
def read_data():

    matrix = []
    for _ in range(0, 3, 1):
        values = input()
        temp = values.split(" ")
        k = []
        for j in temp:
            k.append(j)
        matrix.append(k)
    return matrix
def matrix_check(matrix):
    for element in matrix:
        for j in element:
            if j == 'x' or j == 'o' or j == '.':
                pass
            else:
                return False
    return True
def matrix_game(matrix):
    element_x = 0
    element_o = 0
    element_dot = 0
    for element in matrix:
        for j in element:
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

def main():
    """ main function of the matrix-operation"""
    # read matrix
    mx = read_data()
    tictokto_matrix = matrix_check(mx) and matrix_game(mx)
    win = None
    win = row_check(mx)
    if matrix_check == True:
        if win == None:
            win = col_check(mx)
        if win == None:
            win = diagonal_check(mx)
        if win == None:
            print("draw")
        else:
            print(win)

    else:
        if not row_check(mx):
            print("invalid input")
        if  not matrix_game(mx):
            print("invalid game")

if __name__ == '__main__':
    main()
