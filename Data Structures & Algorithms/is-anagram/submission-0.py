class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hsh={}
        for i in range(len(s)):
            hsh[s[i]]=hsh.get(s[i],0)+1
            hsh[t[i]]=hsh.get(t[i],0)-1
        for val in hsh.values():
            if val==0:
                continue
            else:
                return False
        return True
        
        