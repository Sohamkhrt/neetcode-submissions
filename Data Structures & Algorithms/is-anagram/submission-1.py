class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sList = {}
        tList = {}

        for x in s:
            sList[x] = sList.get(x, 0) + 1
        for y in t:
            tList[y] = tList.get(y, 0) + 1
        
        for z in sList.keys():
            if sList[z] != tList.get(z, 0):
                return False
        
        return True