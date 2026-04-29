class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        answer = 0
        for op in operations:
            if op == "C":
                pop = stack.pop()
                answer-=pop
            elif op == "D":
                stack.append(stack[-1]*2)
                answer+=stack[-1]
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
                answer+=stack[-1]
            else:
                stack.append(int(op))
                answer+=int(op)

        return answer