https://leetcode.com/problems/group-anagrams/

use prime number to encode


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        res = []
        groupMap = defaultdict(list)
        for s_str in strs:
            key = 1
            for s_char in s_str:
                key *= prime[ord(s_char) - ord('a')]
            groupMap[key].append(s_str)
        for key, value in groupMap.items():
            res.append(value)
        return res



from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for inputStr in strs:
            key = ''.join(sorted(inputStr))
            groups[key].append(inputStr)
        res = []
        for key, value in groups.items():
            res.append(value)
        return res