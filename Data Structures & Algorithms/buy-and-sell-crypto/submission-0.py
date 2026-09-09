class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        mprofit=0
        for right in range(1, len(prices)):
            if prices[left]>prices[right]:
                left=right
            else:
                mprofit=max(mprofit,prices[right]-prices[left])
        return mprofit
        