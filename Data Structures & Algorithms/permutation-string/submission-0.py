class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        size=len(s1)
        for right in range(size-1, len(s2)):#window size isk=len(s1),
            if left<=len(s2)-size:
                if sorted(s2[left:right+1]) == sorted(s1):
                    return True
                left+=1
            else:
                break
        return False 

        