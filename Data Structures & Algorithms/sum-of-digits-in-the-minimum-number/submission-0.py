class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        smallest = min(nums)
        digit_sum = 0

        while smallest > 0:
            mod = smallest % 10
            
            digit_sum += mod

            smallest //= 10    
        
        if digit_sum % 2 == 0:
            return 1
        return 0
