N=int(input())
R=input()
C=input()

def fill_board(N, R, C):
    board = [['.' for _ in range(N)] for _ in range(N)]
    
    # Place the initial characters based on R and C
    for i in range(N):
        board[i][0] = R[i]
        board[0][i] = C[i]
    
    # Helper function to get the missing character in a row or column
    def missing_char(s):
        for ch in 'ABC':
            if ch not in s:
                return ch
        return None
    
    # Place the missing characters in the board
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                # Find the missing character in the row and column
                row_chars = set(board[i])
                col_chars = set(row[j] for row in board)
                common_missing_chars = {'A', 'B', 'C'} - row_chars - col_chars
                
                if len(common_missing_chars) == 1:
                    board[i][j] = common_missing_chars.pop()
                else:
                    # If it's not possible to place a character, return "No"
                    return "No", None
    
    return "Yes", board
status, board = fill_board(N, R, C)
print(board)