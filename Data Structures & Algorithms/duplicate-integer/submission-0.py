class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for v in dict.values():
            if v > 1:
                return True

        return False 