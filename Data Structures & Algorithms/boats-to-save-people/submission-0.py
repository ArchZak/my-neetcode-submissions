class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #input: int array of people where i is the weight of the person, and limit
        #output: min num of boats to carry people 

        #you have infinite number of boats where each boat has weight limit
        #each boat can carry at most 2 people at the same time if ther weight is at most lim
        
        #going to sort the array
        #going to do two pointer through array using left and right
        #if l+r <= limit, move both pointers up and add to boat
        #if l+r > limit, only move right pointer down

        #1,2,2,3,3 with lim 3
        #we have boat [3] 1+3
        #we have boat [3] 1+3
        #we have boat [1,2] 1+2
        #we have boat [2]


        people.sort()
        left, right = 0, len(people)-1
        answer = 0

        while left <= right:
            if people[left]+people[right] <= limit:
                answer+=1
                left+=1
                right-=1
            else:
                answer+=1
                right-=1


        return answer