class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        for op in operations:
            if op == "+":
                result += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                result -= stack.pop()
            elif op == "D":
                result += (2 * stack[-1])
                stack.append(2 * stack[-1])
            else:
                result += int(op)
                stack.append(int(op))
        
        return result

        

