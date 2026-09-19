class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        right=len(nums)-1
        
        while right>0 and nums[right]<=nums[right-1]:
            right-=1
        pivot=right-1 #found the pivot
        if pivot!= -1:
            right=len(nums)-1
            while nums[right]<= nums[pivot]:
                right-=1 #found the swap
            nums[right],nums[pivot]=nums[pivot],nums[right]

        #everything after pivot is descending, so make it ascending by reversing
        start=pivot+1
        end= len(nums)-1
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        return nums
    
    
    




      
        