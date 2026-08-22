class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsh=set()
        for item in nums:
            if item in hsh:
                return True
            hsh.add(item)
        return False