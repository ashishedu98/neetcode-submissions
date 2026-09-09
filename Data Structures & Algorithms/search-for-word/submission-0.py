class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row,col,itr):
            if itr == len(word):
                return True
            if (row<0 or row >= len(board) or col<0 or col >= len(board[0])
                or word[itr] != board[row][col] or board[row][col] == '#'):
                return False

            board[row][col] ='#'
            res = (dfs(row+1, col, itr+1) or dfs(row-1, col, itr+1) 
                or dfs(row, col+1, itr+1) or dfs(row, col-1, itr+1))
            board[row][col] = word[itr]
            return res

        for r in range (len(board)):
            for c in range (len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False