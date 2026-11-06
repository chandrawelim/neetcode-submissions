class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        # get total count of appearance
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        # set max
        result = []
        for _ in range(k):
            best_key = None
            best_count = 0
            for key, v in dict.items():
                if v > best_count:
                    best_count = v
                    best_key = key
            result.append(best_key)
            dict[best_key] = 0

        return result