def KingMoves(x, y, color, board):
    possibleMoves=[] 

    for i in range(-1,2): 
        if y+(1-abs(i)) > -1 and y+(1-abs(i)) < 8 and x+i > -1 and x+i < 8: 
            if board[y+(1-abs(i))][x+i] == None or board[y+(1-abs(i))][x+i].color != color:
                possibleMoves.append([x+i, y+(1-abs(i))])
        if y-(1-abs(i)) > -1 and y-(1-abs(i)) < 8 and x+i > -1 and x+i < 8: 
            if board[y-(1-abs(i))][x+i] == None or board[y-(1-abs(i))][x+i].color != color:
                possibleMoves.append([x+i, y-(1-abs(i))])
        if y+i > -1 and y+i < 8 and x+i > -1 and x+i < 8: 
            if board[y+i][x+i] == None or board[y+i][x+i].color != color:
                possibleMoves.append([x+i, y+i])
        if y-i > -1 and y-i < 8 and x+i > -1 and x+i < 8: 
            if board[y-i][x+i] == None or board[y-i][x+i].color != color:
                possibleMoves.append([x+i, y-i])

    return possibleMoves #return all possible moves