https://leetcode.com/problems/palindrome-pairs/

#build a suffix tree, then search with normal word order,
#if we can find a end of word when search ends, its a palindrome pair
#also we can form pairs with all remaining part words that are palindromes
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        rootLevel = self.buildTrie(words)
        res = []
        



        for i in range(len(words)):
            word = words[i]
            currentLevel = rootLevel
            # #handle special case where word is empty
            # if '#' in currentLevel:
            #     for index in currentLevel['#']:
            #         if self.isPalindrom(word, len(word) - 1):
            #             res.append([i, index])
            #             res.append([index, i])

            for j in range(len(word)):
                letter = word[j]
                if letter in currentLevel:
                    currentLevel = currentLevel[letter]
                else:
                    #if we are at end of suffix
                    if '#' in currentLevel:
                        #check if remaining prefix is palindrom
                        if self.isPalindrom(word, j, len(word) - 1):
                            res.append[[i, currentLevel['#']]]
                    break
            else:
                #we have res part palindrom indices
                if 'resPart' in currentLevel:
                    for index in currentLevel['resPart']:
                        if i != index:
                            res.append([i, index])
                        

        return res



    #check if prefix of word till index is palindrom
    #O(K)
    def isPalindrom(self, word, i, j):
        while i <= j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True

    #build a suffix tree such that key value is
    #value = (isEndOfWord, [indices that res of word is palindrom])
    #O(n * k * k)
    def buildTrie(self, words):
        rootLevel = {}
        for x in range(len(words)):
            word = words[x]
            #start with rootLevel
            currentLevel = rootLevel
            #reverse to get a suffix tree
            for i in range(len(word) - 1, -1, -1):
                letter = word[i]
                if letter not in currentLevel:
                    currentLevel[letter] = {}
                currentLevel = currentLevel[letter]
                #if res part is palindrom, we save the indice
                if self.isPalindrom(word, 0, i - 1):
                    if 'resPart' not in currentLevel:
                        currentLevel['resPart'] = [x]
                    else:
                        currentLevel['resPart'].append(x)
            #end of word, save indices
            currentLevel['#'] = [x]
          
        return rootLevel


