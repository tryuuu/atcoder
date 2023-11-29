A = [list(map(int, input().split())) for _ in range(9)]
def sudoku(board):
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if board[i][j] in row or board[j][i] in col:
                return 'No'
            row.add(board[i][j])
            col.add(board[j][i])
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = set()
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] in block:
                        return 'No'
                    block.add(board[i+k][j+l])
    
    return 'Yes'
a=sudoku(A)
print(a)
