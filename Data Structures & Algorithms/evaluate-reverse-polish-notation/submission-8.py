class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #input: tokens with arithmetic in reverse polish notation
        #output: return the answer that evaluates the expression

        #ints or basic math, assume divisim truncates to 0, not -infinity

        #append numbers to a stack, once you encounter a op, do the operator
        #then push the number back onto the stack
        #ROUND TO 0, NOT NEGATIVE INFINITY. meaning int(b/a), b//a

        #1,2
        #3 post addition
        #3,3
        #9, post multi
        #9,4
        #5, post sub

        stack = []

        for token in tokens:
            if token == "+":
                a,b=stack.pop(),stack.pop()
                stack.append(a+b)
            elif token == "-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif token == "*":
                a,b=stack.pop(),stack.pop()
                stack.append(a*b)
            elif token == "/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))

        return stack[0]