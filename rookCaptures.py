"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        transpose = zip(*board)
        c = 0
        
        def findPawns(temp):
            
            rindex = temp.index('R')
            r = 0
            lower = rindex - 1
            while lower > 0:
                if temp[lower] == 'p':
                    r += 1
                    lower = 0
                elif temp[lower] == 'B':
                    lower = 0
                lower -= 1 
            
            higher = rindex + 1
            while higher <= 7:
                if temp[higher] == 'p':
                    r += 1
                    higher = 8
                elif temp[higher] == 'B':
                    higher = 8
                higher += 1 
                
            return r     
    
        for each in board:
            if 'R' in each:
                c += findPawns(each)

        for each in transpose:
            if 'R' in each:
                c += findPawns(each)
            
        return c
