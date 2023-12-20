def KnightMoves(x, y, color, board):
    possibleMoves=[] 


    if y> 0 and x > 1: 
        if board[y-1][x-2] == None or board[y-1][x-2].color != color: 
            possibleMoves.append([x-2, y-1])
    if y < 7 and x > 1: 
        if board[y+1][x-2] == None or board[y+1][x-2].color != color: 
            possibleMoves.append([x-2, y+1])
    if y > 1 and x > 0: 
        if board[y-2][x-1] == None or board[y-2][x-1].color != color: 
            possibleMoves.append([x-1, y-2])
    if y < 6 and x > 0: 
        if board[y+2][x-1] == None or board[y+2][x-1].color != color: 
            possibleMoves.append([x-1, y+2])

    if y < 7 and x < 6: 
        if board[y+1][x+2] == None or board[y+1][x+2].color != color: 
            possibleMoves.append([x+2, y+1])
    if y > 0 and x < 6: 
        if board[y-1][x+2] == None or board[y-1][x+2].color != color: 
            possibleMoves.append([x+2, y-1])
    if y < 6 and x < 7: 
        if board[y+2][x+1] == None or board[y+2][x+1].color != color: 
            possibleMoves.append([x+1, y+2])
    if y > 1 and x < 7: 
        if board[y-2][x+1] == None or board[y-2][x+1].color != color: 
            possibleMoves.append([x+1, y-2])

    return possibleMoves #return all possible moves