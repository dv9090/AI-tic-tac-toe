
def print_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])


"""
what does this do??
"""

def check_winner(board, player):
    win_positions = [(0,1,2), (3,4,5), (6,7,8),
                     (0,3,6), (1,4,7), (2,5,8),
                     (0,4,8), (2,4,6)]
    return any(all(board[i] == player for i in pos) for pos in win_positions)



def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    
    if ' ' not in board:
        return 0
    

    if is_maximizing: 
        best_score = -float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score
    

    else:
        best_score = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score


def best_move(board):
    move = None
    best_score = -float('inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '

            if score > best_score: 
                best_score = score
                move = i
    
    return move


board = [' ' for _ in range(9)]


while True:
    print_board(board)
    move = int(input("Your move (0-8): "))
    if board[move] != ' ':
        print("Invalid move. Try again.")
        continue
    board[move] = 'X'

    if check_winner(board, 'X'):
        print_board(board)
        print("You win!")
        break
    if ' ' not in board:
        print_board(board)
        print("Draw!")
        break

    ai_move = best_move(board)
    board[ai_move] = 'O'
    print(f"AI plays at {ai_move}")
    
    if check_winner(board, 'O'):
        print_board(board)
        print("AI wins!")
        break
    if ' ' not in board:
        print_board(board)
        print("Draw!")
        break
