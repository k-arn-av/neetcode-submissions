class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0;
        setSave=set(nums)
        total=0
        for num in setSave:
            if num-1 not in setSave:
                current=1
                j=1
                while num+j in setSave:
                    current+=1
                    j+=1
                total=max(total,current)
        return total

        


        
