https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        reversedS = s[::-1]
        res = []
        i = j = 0
        n = len(reversedS)
        def writeToRes(i, j):
            word = ""
            for x in range(j, i - 1, -1):
                word += reversedS[x]
            if word:
                res.append(word)
        while (i < n):
            #find first non space, or bring i, j to save position
            while (i < j or (i < n and reversedS[i] == ' ')):
                i += 1; # skip spaces
            #find first space after word, or bring i, j to save position
            while (j < i or (j < n and reversedS[j] != ' ')):
                j += 1; # skip non spaces
            writeToRes(i, j - 1)
        print(res)
        return " ".join(res)


            
