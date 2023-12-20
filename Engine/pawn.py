def PawnMoves(x, y, color, board):
    #determine which direction pawn can move it based on its color
    if color=="white": 
        direction=-1
    elif color=="black": 
        direction=1

    possibleMoves=[] 

    if color=="black" and y==1 or color=="white" and y==6: 
        if board[y+(direction*2)][x] == None:
            possibleMoves.append([x, y+(direction*2)])

    if  x<7 and board[y+direction][x+1] != None and board[y+direction][x+1].color != color:  
        possibleMoves.append([x+1, y+direction])

    if x>0 and board[y+direction][x-1] != None and board[y+direction][x-1].color != color:  
        possibleMoves.append([x-1, y+direction])

    if board[y+direction][x] == None: 
        possibleMoves.append([x, y+direction])

    return possibleMoves #return all possible moves