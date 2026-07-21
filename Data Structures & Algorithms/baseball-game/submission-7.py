class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0

        for operation in operations:
            if operation == "D":
                stack.append(stack[-1] * 2)
                sum += stack[-1]
            elif operation == "C":
                sum -= stack[-1]
                stack.pop()
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
                sum += stack[-1]
            else:
                stack.append(int(operation))
                sum += stack[-1]

        return sum