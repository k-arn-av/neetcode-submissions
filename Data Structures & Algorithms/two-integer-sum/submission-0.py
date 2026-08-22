class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in hsh:
                return [hsh[compliment], i]
            hsh[nums[i]]=i
        return False

            