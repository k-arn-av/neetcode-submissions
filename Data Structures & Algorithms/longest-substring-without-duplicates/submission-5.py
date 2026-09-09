class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxlen=0
        hsh=set()

        for right in range(len(s)):
            while s[right] in hsh:
                hsh.remove(s[left])
                left+=1
        
            hsh.add(s[right])
            maxlen=max(right-left+1, maxlen)

        return maxlen
        