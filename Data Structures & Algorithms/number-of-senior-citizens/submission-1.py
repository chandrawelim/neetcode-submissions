class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output = 0
        for item in range(len(details)):
            age = details[item][11:13]

            if int(age) > 60:
                output += 1
        
        return output
