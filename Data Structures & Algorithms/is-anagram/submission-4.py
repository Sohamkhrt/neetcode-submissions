class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        smap,tmap = {},{}

        for x in range(len(s)):
            smap[s[x]] = smap.get(s[x],0) + 1
            tmap[t[x]] = tmap.get(t[x],0) + 1 
        for c in smap:
            if smap[c] != tmap.get(c,0):
                return False
        return True 

