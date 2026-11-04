class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unique_list = sorted(set(nums))

        nums[:len(unique_list)] = unique_list

        return len(unique_list)