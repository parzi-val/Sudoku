with open('example.txt','r') as file:
    problem = file.readline()[:-1]

val = list(map(int, list(problem)))

thriceOver = lambda prev: [prev[i:i + 9] for i in range(0, len(prev) - 2, 9)]
printable = lambda board: [print(*i) for i in board]

flatten = lambda board: [i for row in board for i in row]

cmp = lambda T: 0 if 0 <= T < 3 else 3 if 3 <= T < 6 else 6
find3by3 = lambda coords: (cmp(coords[0]), cmp(coords[1]))

reduce = lambda board : list(filter(lambda i:i != 0,flatten(board)))
union = lambda *sets : list(set(sets[0]).union(set(sets[1])).union(set(sets[2])))

rowSet = lambda board,x : [board[x][j]  for j,_ in enumerate(board[x]) if board[x][j] != 0]
colSet = lambda board,y : [board[i][y]  for i,_ in enumerate(board) if board[i][y] != 0]
x33Set = lambda board,TLx,TLy: reduce([row[TLy:TLy+3] for row in board[TLx:TLx+3]])


board = thriceOver(val)


def zero(board):
    i = 0
    zeroes = []
    for k,v in enumerate(flatten(board)):
        if v == 0:
            zeroes.append((i,k%9))
        if k%9 == 8:
            i+=1 

    for i in zeroes:
        yield i


def gen(board,coords):
    x,y = coords
    ignoreNums = union(rowSet(board,x),colSet(board,y),x33Set(board,*find3by3(coords)))
    
    for i in range(1,10):
        if i not in ignoreNums:
            yield i

            
def sudoku(board):
    try:
        target = next(zero(board))
    except StopIteration:
        return True

    targetX,targetY = target

    for k in gen(board,target):
        board[targetX][targetY] = k
        if sudoku(board):
            return True
        board[targetX][targetY] = 0
    
    return False


printable(board)
print("\n")

sudoku(board)
printable(board)