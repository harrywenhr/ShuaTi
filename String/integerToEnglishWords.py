https://leetcode.com/problems/integer-to-english-words/
class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        #return a list of english words for that number
        #start from thousand, we have 1000 * 1000 = one million
        #1 million * 1 million = 1 billion
        def words(n):
            if n == 0:
                return []
            if n <= 19:
                return [to19[n - 1]]
            if n < 100:
                tensNumber = n // 10
                tensStr = tens[tensNumber - 2]
                digits = words(n % 10)
                return [tensStr] + digits
            if n < 1000:
                hundredNumber = n // 100
                hundreds = words(hundredNumber)
                tensList = words( n % 100)
                return hundreds + ['Hundred'] + tensList
            for index, word in enumerate(('Thousand', 'Million', 'Billion')):
                powerNumber = index + 2
                #powerNumber from 2,3,4 = 1000^2 = one million 1000^3 = one billion
                #1000 ^ 4 = 1 thousand billion
                #e.g if its less than 1 million, 
                numberBound = 1000 ** powerNumber
                numberDivider = 1000 ** (powerNumber - 1)
                if n < numberBound:
                    #if less than 1000^2, we chose thousand
                    #if less than 1000^3, we chose million
                    #if less than 1000^4, we chose billion
                    #at most is 3 billion
                    firstPart = words(n // numberDivider)
                    remainsPart = words(n %  numberDivider)
                    return firstPart + [word] + remainsPart

        return ' '.join(words(num)) or "Zero"

