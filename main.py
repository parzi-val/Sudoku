rows = cols = 9

with open('example.txt','r') as file:
    problem = file.readline()[:-1]


val = list(map(int, list(problem)))

thriceOver = lambda prev: [prev[i:i + 9] for i in range(0, len(prev) - 2, 9)]
printable = lambda board: [print(*i) for i in board]

topLefts = reversed([(i, j) for i in range(0, 7, 3) for j in range(0, 7, 3)])
cmp = lambda T: 0 if 0 <= T < 3 else 3 if 3 <= T < 6 else 6
find3by3 = lambda coords: (cmp(coords[0]), cmp(coords[1]))

negation = lambda *states: [not any(state) for state in states]

def gen():
    for i in range(1, 10):
        yield i

def zero(board):
    x, y = 0, -1
    while x < rows:
        while y < cols - 1:
            y += 1
            if board[x][y] == 0:
                yield (x, y)
        y = -1
        x += 1

def validState(board, coords):
    x, y = coords
    target = board[x][y]
    thisX, thisY = find3by3(coords)

    rowState = [board[x][j] == target and j != y for j, _ in enumerate(board[x])]
    colState = [board[i][y] == target and i != x for i, _ in enumerate(board)]
    threeByThree = [board[i][j] == target and i != x and j != y for i in range(thisX, thisX + 3)
                    for j in range(thisY, thisY + 3)]

    return all(negation(rowState, colState, threeByThree))

board = thriceOver(val)

def sudoku(board):
    try:
        target = next(zero(board))
    except StopIteration:
        return True
    
    targetX, targetY = target

    for k in gen():
        board[targetX][targetY] = k
        if validState(board, target):
            if sudoku(board):
                return True
        board[targetX][targetY] = 0

    return False


printable(board)
print("\n")

sudoku(board)
printable(board)
