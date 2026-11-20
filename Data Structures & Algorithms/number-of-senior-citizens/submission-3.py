class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output = 0
        for item in details:
            if int(item[11:13]) > 60:
                output += 1
        return output
