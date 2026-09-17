class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:#take two freq hashmaps and check 
        left=0
        csize=len(s1)
        hsh1=Counter(s1)
        hsh2={}
        for right in range(len(s2)):

            hsh2[s2[right]]=hsh2.get(s2[right], 0)+1

            if (right-left+1)> csize:
                hsh2[s2[left]]=hsh2.get(s2[left],0)-1
                if hsh2[s2[left]]==0:
                    del hsh2[s2[left]]
                left+=1
            
            if hsh1==hsh2:
                return True
        return False
                
                
            



        