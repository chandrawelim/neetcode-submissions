class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = { }
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        max_appear = 0
        output = None
        for k,v in dict.items():
            if v > max_appear:
                max_appear = v
                output = k
        
        return output