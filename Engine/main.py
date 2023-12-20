import piece

#create board
board = []
for i in range(8):
    board.append([None,None,None,None,None,None,None,None]) 

#setup starting board pos
boardSetUp = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
for i in range(8): 
    board[0][i] = piece.Piece(i, 0, "black", boardSetUp[i])
    board[1][i] = piece.Piece(i, 1, "black", "pawn")
    board[7][i] = piece.Piece(i, 7, "white", boardSetUp[i])
    board[6][i] = piece.Piece(i, 6, "white", "pawn")

