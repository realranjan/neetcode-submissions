class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set) # dict inisde it is empty set {5:{0,1}}
        rows=defaultdict(set)
        squares=defaultdict(set)

        for i in range(9):  # rows
            for j in range(9): # columns 9 cause we know 9 rows and col soo
                if board[i][j]=='.': # if . means empty box means valid so we continue
                    continue 
                if ( board[i][j] in rows[i] or # if the values in say (0,0) in rows or col or 
                    board[i][j] in cols[j] or  #we made separete boxes my 
                    board[i][j] in squares[(i//3 ,j//3 )]): # r /3 and col by 3 if present in that its not sudoku
                    return False

                cols[j].add(board[i][j]) # here we add the numbers if not in the rows ad col and squares 
                rows[i].add(board[i][j])
                squares[(i // 3 ,j // 3)].add(board[i][j])

        return True
                  
        
'''Col 0-2    Col 3-5    Col 6-8
        ┌────────┬────────┬────────┐
Row 0-2 │ (0,0)  │ (0,1)  │ (0,2)  │
        ├────────┼────────┼────────┤
Row 3-5 │ (1,0)  │ (1,1)  │ (1,2)  │
        ├────────┼────────┼────────┤
Row 6-8 │ (2,0)  │ (2,1)  │ (2,2)  │
        └────────┴────────┴────────┘'''