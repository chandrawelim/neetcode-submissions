class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        output = 0

        while i <= j:
            if nums[i] != val:
                i+=1
                output += 1
            elif nums[j] == val:
                j-=1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j-=1
                output += 1
        return output
