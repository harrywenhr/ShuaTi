https://leetcode.com/problems/candy-crush/
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        board= list(zip(*board[::-1]))  # rotate clockwise 90 degree
        m,n=len(board),len(board[0])

        # repeat crush and drop
        while True:
            candy=set()
            # check every row
            for i in range(m):
                board[i] = list(board[i])
                for j in range(2,n):
                    if board[i][j] and board[i][j]==board[i][j-1]==board[i][j-2]:
                    	#add crushed positions to candy set
                        candy|={(i,j),(i,j-1),(i,j-2)}
            # check every col
            for j in range(n):
                for i in range(2,m):
                    if board[i][j] and board[i][j]==board[i-1][j]==board[i-2][j]:
                        #add crushed positions to candy set
                        candy|={(i,j),(i-1,j),(i-2,j)}
            if not candy: break
            for crushed in candy:
                board[crushed[0]][crushed[1]]=0

            # drop the board, move non-zero to the beginning of each row.
            for i in range(m):
            	#if value is 0(false), we delete that item
                row=list(filter(None,board[i]))
                #we add 0s at the end of the row
                board[i]=row + [0]*(n-len(row))
     
        board=list(zip(*board))[::-1] # rotate counter-clockwise 90 degree
        return board


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #rotate matrix 90 degree
        board= list(zip(*board[::-1]))
        #print(board)
        while True:
            candy = set()
            for i in range(len(board)):
                board[i] = list(board[i])
                for j in range(len(board[0]) - 2):
                    if board[i][j] == board[i][j + 1] == board[i][j + 2] != 0:
                        candy.add((i,j))
                        candy.add((i,j + 1))
                        candy.add((i,j + 2))
            for j in range(len(board[0])):
                for i in range(len(board) - 2):
                    if board[i][j] == board[i + 1][j] == board[i + 2][j] != 0:
                        candy.add((i,j))
                        candy.add((i + 1,j))
                        candy.add((i + 2,j))
            #print(candy)
            if not candy:
                break
            for candy in candy:
                board[candy[0]][candy[1]] = 0
            #print(board)
            for row in range(len(board)):
                newRowArray = list(filter(None, board[row]))
                newRowArray += (len(board[row]) - len(newRowArray)) *[0]
                board[row] = newRowArray
            #print(board)
        #rotate back
        board=list(zip(*board))[::-1]
        return board