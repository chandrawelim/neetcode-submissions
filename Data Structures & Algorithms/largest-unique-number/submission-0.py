class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        dict = {}

        for k,v in enumerate(nums):
            if v in dict:
                dict[v] += 1
            else:
                dict[v] = 1

        result = -1
        for k,v in dict.items():
            if v == 1:
                result = max(result, k)

        return result
