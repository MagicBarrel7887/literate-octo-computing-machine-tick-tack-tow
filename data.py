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





def enter_move(board):
    """# The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision."""
    while True: 
        move = int(input("Please enter a number in the board "))
        if move < 1 or move > 9:
            print('')
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('')
            continue
        elif move == 1:
            board[0][0]='0'
        elif move == 2:
            board[0][1] = '0'
        elif move == 3:
            board[0][2] = '0'
        elif move == 4:
            board[1][0]='0'
        elif move == 5:
            board[1][1]='0'
        elif move == 6:
            board[1][2]='0'
        elif move == 7:
            board[2][0] = '0'
        elif move == 8:
            board[2][1] = '0'
        elif move == 9:
            board[2][2] = '0'



# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares;
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
     print('Checking for if player', sign, "is the winner!")
     if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
         print("player", sign, "is the winner!")
     elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        print("player", sign, "is the winner!")
       


# def draw_move(board):

while True:
    displayBoard(board)
    enter_move(board)
