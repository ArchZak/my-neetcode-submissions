class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #keeping score of game with rules, start with empty record
        #input: strings of ops where ops[i] is ith operation ytou must apply to record
        #int x, record new score of x
        #+ record a new score that's sum of previous two scores
        #D record new score double of previous score
        #C invalide previous score removing it from the record

        #return sum of the array

        #will use a list as a stack to append numbers too
        #will pop if come across a C
        #will add last two if coming across a +
        #will double last item if come across D

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
