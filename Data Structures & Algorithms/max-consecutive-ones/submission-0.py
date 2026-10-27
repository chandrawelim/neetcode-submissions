class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_total = 0
        total = 0
        for i, value in enumerate(nums):
            if value == 1:
                total += 1
                max_total = max(max_total, total)
            else:
                total = 0
            
        return max_total