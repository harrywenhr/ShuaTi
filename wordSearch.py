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
                    if self.dfs(board, row, column, 0, word):
                        return True

                    # if self.recusiveDFS(board, row, column, word, 0):
                    #     return True
        return False
    def recusiveDFS(self, board, currentRow, currentColumn, word, checkingIndex):
        #print("{0} {1} {2} {3}".format(currentRow, currentColumn, checkingIndex))
        if checkingIndex >= len(word):
            return True
        if board[currentRow][currentColumn] == word[checkingIndex]:
            if (checkingIndex + 1) == len(word):
                return True
            tmp = board[currentRow][currentColumn]
            board[currentRow][currentColumn] = "#"
            #visiting neighbors
            for row, column in ((currentRow, currentColumn - 1), (currentRow, currentColumn + 1), (currentRow -1 , currentColumn), (currentRow +1 , currentColumn)):
                if (row < len(board) and row >= 0) and (column < len(board[0]) and column >= 0):
                    if (row, column) != "#":
                        if self.recusiveDFS(board, row, column, word, checkingIndex + 1):
                            return True
            board[currentRow][currentColumn] = tmp
        return False


    def dfs(self, board, row, column, checkingIndex, word):
        #We have a visited Set(), we add a backtracking node after we pop a node(visited)
        #When the node we get is a backtrack, we kownn we visited all its children
        #It may be ok for other Nodes from one level above to visit this one
        #we remove it from visited
        #Visited make sure we dont visit parent again while do DFS search
        dfsStack = [[row, column, checkingIndex, False]]
        visited = set()

        while dfsStack:
            currentElement = dfsStack.pop()
            currentRow, currentColumn, currentCheckingIndex, isBackTrack = currentElement[0], currentElement[1], currentElement[2], currentElement[3]
            if isBackTrack:
                #we remove this node from visited 
                visited.remove((currentRow, currentColumn))
                continue
            visited.add((currentRow, currentColumn))
            #we already checked the current index before we enter dfs search
            if currentCheckingIndex >= (len(word) - 1):
                return True
            #We add a back track node before addinng all its childeren

            dfsStack.append([currentRow, currentColumn, currentCheckingIndex, True])

            #visiting neighbors
            for row, column in ((currentRow, currentColumn - 1), (currentRow, currentColumn + 1), (currentRow -1 , currentColumn), (currentRow +1 , currentColumn)):
                if (row < len(board) and row >= 0) and (column < len(board[0]) and column >= 0):
                    #print("{0} {1} {2} {3}".format(row, column, board[row][column], word[currentCheckingIndex]))
                    if (row, column) not in visited:
                        if board[row][column] == word[currentCheckingIndex + 1]:
                            dfsStack.append([row, column, currentCheckingIndex + 1, False])
        return False

