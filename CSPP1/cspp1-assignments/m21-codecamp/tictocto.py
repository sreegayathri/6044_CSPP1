"""to write a program to check possible outcomes while playing tictactto"""
def row_check(matrix):
    """to check if row has similar values x/o/."""
    if matrix[0][0] == matrix[0][1] == matrix[0][2]:
        return matrix[0][0]
    if matrix[1][0] == matrix[1][1] == matrix[1][2]:
        return matrix[1][1]
    if matrix[2][0] == matrix[2][1] == matrix[2][2]:
        return matrix[2][0]
def col_check(matrix):
    """to check if column has similar values x/o/."""
    if matrix[0][0] == matrix[1][0] == matrix[2][0]:
        return matrix[0][0]
    if matrix[0][1] == matrix[1][1] == matrix[2][1]:
        return matrix[1][1]
    if matrix[0][2] == matrix[1][2] == matrix[2][2]:
        return matrix[0][2]
def diagonal_check(matrix):
    """to check if diagonal has similar values x/o/."""
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[1][1]
def matrix_check(matrix):
    """to check if input has values x/o/."""
    for element in matrix:
        for j in element:
            if j in 'x' or j in 'o' or j in '.':
                pass
            else:
                return False
    return True
def matrix_game(matrix):
    """to check if the game is valid or not with x/o elements with differnceof 1/2"""
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
    if abs(element_x - element_o == 0) and element_dot > 0:
        return False
    return True
def main():
    """ main function of the matrix-operation"""
    win = None
    matrix = []
    for _ in range(0, 3, 1):
        values = input().split(' ')
        temp = []
        for j in values:
            temp.append(j)
        matrix.append(temp)
    tictokto_matrix = matrix_check(matrix) and matrix_game(matrix)
    if tictokto_matrix is True:
        win = row_check(matrix)
        if win is None:
            win = col_check(matrix)
        if win is None:
            win = diagonal_check(matrix)
        if win is None:
            print("draw")
        else:
            print(win)
    else:
        if not matrix_check(matrix):
            print("invalid input")
        if  not matrix_game(matrix):
            print("invalid game")

if __name__ == '__main__':
    main()
