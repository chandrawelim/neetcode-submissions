class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for index, value in enumerate(nums2):
            dict[value] = index

        output = []
        for i in range(len(nums1)):
            if nums1[i] in dict:
                output.append(dict[nums1[i]])
        
        return output