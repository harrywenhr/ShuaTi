https://leetcode.com/problems/word-search/
#DFS search, use one additional stack to save tmp str values and set it back when poping elements
#https://leetcode.com/problems/word-search/discuss/131327/Iterative-Python-Solution
class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        if not board:
            return False
        if not word:
            return False
        for row in range(0, len(board)):
            for column in range(0, len(board[0])):
                if board[row][column] == word[0]:
                    #pass currentChecking Index at word
                    if self.dfs(board, row, column, 1, word):
                        return True
        return False
    def dfs(self, board, row, column, checkingIndex, word):
        #we add element to stack means we visited it, we save it to tmp and set value to #
        dfsStack = [[row, column, checkingIndex]]
        tmp = board[row][column]
        board[row][column] = "#"
        tmpStack = [[row, column, tmp]]
        while dfsStack:
            print(dfsStack)
            currentElement = dfsStack.pop()
            currentRow, currentColumn, currentCheckingIndex = currentElement[0], currentElement[1], currentElement[2]
            if currentCheckingIndex >= len(word):
                return True
            #visiting neighbors
            for row, column in ((currentRow, currentColumn - 1), (currentRow, currentColumn + 1), (currentRow -1 , currentColumn), (currentRow +1 , currentColumn)):
                if (row < len(board) and row >= 0) and (column < len(board[0]) and column >= 0):
                    print("{0} {1} {2} {3}".format(row, column, board[row][column], word[currentCheckingIndex]))
                    if board[row][column] == word[currentCheckingIndex]:
                        dfsStack.append([row, column, currentCheckingIndex + 1])
                        tmp = board[row][column]
                        board[row][column] = "#"
                        tmpStack.append([row, column, tmp])
        for element in tmpStack:
            row, column, value = element[0], element[1], element[2]
            board[row][column] = value
        return False

