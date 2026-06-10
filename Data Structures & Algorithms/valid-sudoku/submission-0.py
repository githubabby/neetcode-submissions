class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [{} for i in range(9)]
        col_map = [{} for i in range(9)]
        box_map = [{} for i in range(9)]

        # ITERATE
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in row_map[i]:
                        return False
                    else:
                        row_map[i][val]=True
                    if val in col_map[j]:
                        return False
                    else:
                        col_map[j][val]=True
                    box_id = 3*(i//3)+(j//3)
                    if val in box_map[box_id]:
                        return False
                    else:
                        box_map[box_id][val]=True
        return True

                    
 