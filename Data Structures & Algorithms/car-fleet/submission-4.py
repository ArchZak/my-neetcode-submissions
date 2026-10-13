class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #input: array of position, speed, and then target position
        #output: number of fleets when driving to target

        #n cars traveling on one way highway -> so move one way
        #given two arrays of position and speed both equal length where i corresponds
        #destination is target miles
        #cars cant pass one another, if they catch up then they drive at same speed of car ahead
        #fleet is nonempty set of cars driving at same speed and pos, single car is fleet

        #constraints:
        #will have at least 1 car
        #target wont be 0 miles
        #cars will be moving
        #nobody will start at target, positions are unique

        #cars can catch up at target, but not after 
        #what if n cars reach target in same time but dont catch up, still n -> go back

        #positions and speeds arent sorted

        #7 4 1 0
        #1 2 2 1

        #3, 5, 10

        #going to need to loop backwards and use a stack
        #at each step we compute remaining hours to destination
        #if we try get a bigger hour, just append it on, can use decimal to keep particular
        #if we try to add a equal or less number
        #a car behind cant affect the car ahead so we loop backward

        cars = sorted([x for x in zip(position, speed)], reverse=True)
        stack = []
        
        for p, s in cars:
            ttd = (target-p)/s

            if not stack or ttd > stack[-1]:
                stack.append(ttd)


        return len(stack)
        

        
        