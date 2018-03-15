
def print_board(board):
    for i in range(4):
        print board[i]

def isSafe(board, r, c):
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if r == i or c == j:
                    return False
                if abs(r-i) == abs(c - j):
                    return False
    return True

def place(board, c):

    if c >= 4:
        return True

    for r in range(4):

        if isSafe(board, r, c):
            board[r][c] = 1
        print r,c
        print_board(board)

        if place(board, c+1):
            return True

        board[r][c] = 0

    return False

def main():
    board = [[0]*4 for i in range(4)]
    print_board(board)
    print
    place(board, 0)
    print_board(board)

if __name__ == '__main__':
    main()
