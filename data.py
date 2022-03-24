board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]


def displayBoard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] + '   |   ' + board[0]
          [1] + '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

    print('|       |       |       |')
    print('|   ' + board[1][0] + '   |   ' + board[1]
          [1] + '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

    print('|       |       |       |')
    print('|   ' + board[2][0] + '   |   ' + board[2]
          [1] + '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


displayBoard(board)
