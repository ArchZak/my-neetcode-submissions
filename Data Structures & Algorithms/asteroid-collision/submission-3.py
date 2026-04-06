class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #input: int array of asteroids where indices is the relative position
        #for each asteroid, the abs value is its size, and the sign is the direciton

        #speed is the same on all, so two in the same dir dont meet
        #this means asteroids only meet if right moving meets left moving in stack
        #so positive in stack, then try to append negative

        #find the state of the asteroids after all collisions
        #smaller one explodes, and both of same size explode

        #have a stack where you add asteroids to them
        #for each asteroid in the array, while stack, a < 0, and stack[-1] is positive
        #if same size, just pop the item and exit the loop
        #if incoming is bigger, pop item from array
        #if incoming is smaller, exit loop
        #then just add to stack when exiting loop is asteroid didnt get destroyed

        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0: #so while item is positive and incoming neg
                if -ast == stack[-1]:
                    ast=0 #incoming destroyed
                    stack.pop()
                elif -ast > stack[-1]:
                    stack.pop()
                elif -ast < stack[-1]:
                    ast=0
            if ast:
                stack.append(ast)
        
        return stack

