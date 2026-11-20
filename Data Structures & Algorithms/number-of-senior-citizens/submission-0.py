class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output = 0
        for item in range(len(details)):
            phone = details[item][0:9]
            gender = details[item][10]
            age = details[item][11:13]
            seat = details[item][13:15]

            if int(age) > 60:
                output += 1
        
        return output
