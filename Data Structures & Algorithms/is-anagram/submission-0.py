class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        dict_two = {}
        for i in t:
            if i in dict_two:
                dict_two[i] += 1
            else:
                dict_two[i] = 1

        return dict == dict_two 