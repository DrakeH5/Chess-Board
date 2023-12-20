import pawn
pawnMoves = pawn.PawnMoves

import bishop
bishopMoves = bishop.BishopMoves

import rook
rookMoves = rook.RookMoves

import knight
knightMoves = knight.KnightMoves

import queen
queenMoves = queen.QueenMoves

import king
kingMoves = king.KingMoves



def findAllMoves(board, specificColor):
    allMoves=[]
    for i in range(8): 
        for j in range(8):
            if board[i][j] != None and board[i][j].color == specificColor: 
                getMoves = eval(board[i][j].type + "Moves")
                allMoves += getMoves(board[i][j].x, board[i][j].y, board[i][j].color, board)
    return allMoves