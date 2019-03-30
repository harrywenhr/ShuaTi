https://leetcode.com/problems/word-search-ii/
#Make pref fix tree, space complexity O(26 * m*n) m = number of words, 
#n = word length
#the dfs, check within bounds in neighbor search
#check if next leaf is #(end char) before go in for neibors
# continue for neibors even if we have a match, aaa, aaab
#if no dup allowed in results, remove end of word mark once a word is found
#
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        Trie = self.makeTrie(words)
        results = []
        path = []
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(board, i, j, Trie, results, path, visited)
        return results

    def helper(self, board, row, column, currentTrieLevel, results, path, visited):
        letter = board[row][column]
        if letter not in currentTrieLevel:
            return
        #visited current valid character
        visited.add((row, column))
        newPath = path + [letter]
        #check if we have a word valid already
        if '#' in currentTrieLevel[letter]:
            results.append(''.join(newPath))
            #we also reset current word as not valid since we have a match
            #in board already
            del currentTrieLevel[letter]['#']
            #we continue for the search as there may be aaa, aaab, aaabb
        for newRow,newColumn in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
            #visit unvisited neighbors
            #make sure within bounds
            if newRow >= 0 and newRow < len(board) and newColumn >= 0 and newColumn < len(board[0]):
                if (newRow, newColumn) not in visited:
                    self.helper(board, newRow, newColumn, currentTrieLevel[letter], results, newPath, visited)
        visited.remove((row, column))
    #dics of dics
    def makeTrie(self, words):
        rootLevel = {}
        for word in words:
            #we get the root level before inserting each word
            currentLevel = rootLevel
            for letter in word:
                if letter not in currentLevel:
                    currentLevel[letter] = {}
                #go to next level
                currentLevel = currentLevel[letter]
            #end of a valid word
            currentLevel['#'] = '#'
        return rootLevel















>>> def make_trie(*words):
...     root = dict()
...     for word in words:
...         current_dict = root
...         for letter in word:
                if letter not in current_dict:
                    #if new letter in this level
                    #set a new dictionary
                    current_dict[letter] = {}
                #next dictionay is the currentdictionay with letter
                current_dict = current_dict[letter]
            #mark the word ennd
...         current_dict[_end] = _end
...     return root
