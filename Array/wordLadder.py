https://leetcode.com/problems/word-ladder/
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.


shortst path in graph means bfs
bfs, adjacent nodes differ only by one letter, need to find the number 
of levels to destination

we pre prosses the list such that its in following format {a*b:[adb,acb,afb]}
so when we have a start node, we can easily find its adjacent nodes


from collections import deque
from collections import deque
class Solution:

    #we use 2 bfs search, meet in the middle
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mapStr = {}
        for word in wordList:
            for i in range(len(word)):
                tempWord = word[:i] + "*" + word[i + 1:]
                if tempWord in mapStr:
                    mapStr[tempWord].append(word)
                else:
                    mapStr[tempWord] = [word]

        bfsQueue = deque([[beginWord, 1]])
        visited = set()
        while bfsQueue:
            currentItem = bfsQueue.popleft()
            #add to visited

            currentWord = currentItem[0]
            currentLevel = currentItem[1]
            visited.add(currentWord)
            #Find all neibors and add it
            for i in range(len(currentWord)):
                tempWord = currentWord[:i] + "*" + currentWord[i + 1:]
                if tempWord in mapStr:
                    for word in mapStr[tempWord]:
                        if word not in visited:
                            # we found our destination, we return
                            if word == endWord:
                                return currentLevel + 1
                            bfsQueue.append([word, currentLevel + 1])
        return 0

#practiced
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordMap = {}
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + "*" + word[i+1:]
                if template in wordMap:
                    wordMap[template].append(word)
                else:
                    wordMap[template] = [word]
        #bfs
        #word, and current level
        bfsQ = deque([[beginWord, 1]])
        visited = set()
        while bfsQ:
            currentItem = bfsQ.popleft()
            currentWord = currentItem[0]
            currentLevel = currentItem[1]
            visited.add(currentWord)
            if currentWord == endWord:
                return currentLevel
            for i in range(len(currentWord)):
                template = currentWord[:i] + "*" + currentWord[i+1:]
                if template in wordMap:
                    for neighborWord in wordMap[template]:
                        if neighborWord not in visited:
                            bfsQ.append([neighborWord, currentLevel + 1])
        return 0



