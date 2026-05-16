from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        column = defaultdict(list)
        square = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] == "." :continue
                
                if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in square[(i//3,j//3)] :
                    return False
                row[i].append(board[i][j])
                column[j].append(board[i][j])
                square[(i//3,j//3)].append(board[i][j])
        return True