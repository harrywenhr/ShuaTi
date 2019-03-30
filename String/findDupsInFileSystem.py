https://leetcode.com/problems/find-duplicate-file-in-system/
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fileMap = defaultdict(list)
        res = []
        for path in paths:
            items = path.split(" ")
            for item in items[1:]:
                actualFilePath = items[0] + "/" + item.split("(")[0]
                fileContent = item.split("(")[1].split(")")[0]
                fileMap[fileContent].append(actualFilePath)


        for v in fileMap.values():
            if len(v) >= 2:
                res.append(v)
        return res

