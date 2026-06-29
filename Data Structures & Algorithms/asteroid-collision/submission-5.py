class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #input: list of ints that are positive if right and negative if left and is size
        #output: remaining list after collisions

        #smaller explodes, both explode if same size
        #asteroids move at same speed so they wont meet

        #if you come across a positive num, itll go right, and rest on top of the stack
        #if you come across negative, itll smash left and keep breaking into the stack
        
        #so the only way asteroids would collide is if negative -> positive

        stack = [asteroids[0]]

        for i in range(1,len(asteroids)):
            curr_a = asteroids[i]
            while stack:
                curr_s = stack[-1]
                if curr_s > 0 and curr_a < 0:
                    if abs(curr_a) > curr_s: # if ast is bigger than stack, pop stack, keep going
                        stack.pop()
                    elif abs(curr_a) < curr_s: # if ast is smaller than stack, just break
                        break 
                    else: # if both break, pop, then break
                        stack.pop()
                        break
                else:
                    stack.append(curr_a)
                    break
            else:
                stack.append(curr_a)
            
        return stack
