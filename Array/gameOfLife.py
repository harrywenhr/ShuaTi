#https://leetcode.com/problems/game-of-life/
#We scan matrix twice
#king thing is when we flip the number, we maintain its property odd is live
#even is dead
#First time we get the number of odd numbers in neibors, then if we need to
# Flip current number from 0 -> 1, we set it to 2, if 1 -> 0 we set it to 3
#On second scan, if number == 2 we set it to 1, if 3 we set it to 0


class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        # """
        # Do not return anything, modify board in-place instead.
        # """
        if len(board) < 1:
            return
        for i in range(0, len(board[0])):
            for j in range(0, len(board)):
                oddNumber = self.numberOfOddsInNeibor(board, i, j)
                if board[j][i] % 2 == 1:
                    if oddNumber < 2 or oddNumber > 3:
                        board[j][i] += 2
                else:
                    if oddNumber == 3:
                        board[j][i] += 2
        for i in range(0, len(board[0])):
            for j in range(0, len(board)):
                if (board[j][i] % 2 == 1) and board[j][i] != 1:
                    board[j][i] = 0
                if (board[j][i] % 2 == 0) and board[j][i] != 0:
                    board[j][i] = 1
    def numberOfOddsInNeibor(self, board, x, y):
        oddNumber = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not (i == x and j == y):
                    if i >= 0 and i < len(board[0]) and j >= 0 and j < len(board):
                        if board[j][i] % 2 == 1:
                            oddNumber += 1
        return oddNumber


#practice should be no need