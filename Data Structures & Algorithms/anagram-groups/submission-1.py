class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            key = "".join(sorted(i))
            
            dict.setdefault(key, []).append(i)


        return list(dict.values())