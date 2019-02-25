
https://leetcode.com/problems/word-ladder-ii/

shortst path in graph means bfs
bfs, adjacent nodes differ only by one letter, need to find the number of levels to destination

we pre prosses the list such that its in following format {a*b:[adb,acb,afb]}
so when we have a start node, we can easily find its adjacent nodes

use bfs first to build a word transform map {word: [neibors]}
then use dfs from end to start to produce all possiable paths


defaultdict(<class 'list'>, {'dog': ['cog'], 'log': ['cog'], 'lot': ['log'], 'dot': ['dog'], 'hot': ['dot', 'lot'], 'hit': ['hot']})


from string import ascii_lowercase
from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        def backtrack(results, path, word):
            path.append(word)
            if word == endWord:
                results.append(path[:])
            else:
                for next_word in graph[word]:
                    backtrack(results, path, next_word)
            path.pop()
            
        unvisited = set(wordList)
        if endWord not in unvisited:
            return []
        #we travel from bottom of the graph
        unvisited.add(beginWord)
        unvisited.remove(endWord)
        visit = set([endWord])
        graph = defaultdict(list)
        while visit:
            #nex visit is all words
            next_visit = set()
            found = False
            for word in visit:
                for i in range(len(word)):
                    first, second = word[:i], word[i+1:]
                    for c in ascii_lowercase:
                        new_word = first + c + second
                        if new_word not in unvisited:
                            continue
                        if new_word == beginWord:
                            found = True
                        #new word may be same here thats why we use a set for next visit
                        # two lower level nodes may point to same upper level node
                        next_visit.add(new_word)
                        #We construct our graph in such a way that all neibor words points to end word, then we go up
                        #From bottom to top, since we only care paths end at end word
                        graph[new_word].append(word)
            # Finished the current iteration.
            if found:
                break
            #when the current ladder was completed, delete the visited words from unvisited.
            #we remove the visited nodes from current unvisited words
            unvisited = unvisited.difference(next_visit)
            #next time we visit words from one level up
            visit = next_visit
        # res = []
        # backtrack(res, [], beginWord)
        # return res
        print(graph)
        # return self.dfsIterative(beginWord, endWord, graph)
        results = []
        path = []
        self.dfsRecurive(beginWord, endWord, neiborsMap, path, results)
        return results


    def dfsRecurive(self, word, endWord, neiborsMap, currentPath, results):
        currentPath.append(word)
        if word == endWord:
            #important, we must not use reference, we need the actual value
            results.append(list(currentPath))
        else:
            if word in neiborsMap:
                for neiborWord in neiborsMap[word]:
                    self.dfsRecurive(neiborWord, endWord, neiborsMap, currentPath, results)
        currentPath.pop()

    def dfsIterative(self, beginWord, endWord, neiborsMap):
        #we now use dfs to get all possiable words with minStep
        #Start from end word with backtrack node
        #when we hit a backtrack, we remove it from visited to allow other paths to use it
        results = []
        dfsStack = [(beginWord, False)]
        visited = set()
        while dfsStack:
            currentWordItem = dfsStack.pop()
            currentWord = currentWordItem[0]
            isBackTrack = currentWordItem[1]
            #print(currentWordItem)
            if isBackTrack:
                visited.remove(currentWord)
                continue

            visited.add(currentWord)
            #We add a back track node before addinng all its childeren

            dfsStack.append((currentWord, True))
            if currentWord in neiborsMap:
                for neiborWord in neiborsMap[currentWord]:
                    if neiborWord not in visited:
                        #we found our path
                        if neiborWord == endWord:
                            path = list(visited) + [endWord]
                            results.append(path)
                        dfsStack.append((neiborWord, False))
        return results