class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #input: #given array of ints where each value is cost of taking a step there
        #output: #return minimum cost to reach the top, so just past the last index in cost

        #general
        #after paying the cost, you can take 1 or 2 steps up
        #can start at 0 or 1 floor
        #decision tree at each step because you either do 1 or 2 (backtracking via dfs)
        
        #constraints + edge cases
        #will have at least 2 steps
        #cost is nonnegative
        #0 or 1, need to choose -> tracking doing bottom up will solve

        #tests + examples
        #[1,2,3], output = 2
        #[4, 2, 3]

        #[1,2], output = 1
        #[1,2]

        #english
        #need to dfs through the decisions we can make to reach the top using index `i`
        #base case: if out of bounds it's over return 0
        #recursive case: do a dfs with i+1 and i+2
        #cache so each value is how much it costs to reach the top, put the min of dfs(i+1),dfs(i+2)

        #pseudo
        #cache = [-1]*len(cost)
      #def dfs(i):
        #   if i >= len(cost) return cost[i]
        #   if i in cache != -1 return cache[i]
        #   cache[i] = min(dfs(i+1),dfs(i+2))
        #   return cost[i]

        #return min(index 0 or 1)

        cache = [-1]*len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]

            one, two = dfs(i+1)+cost[i],dfs(i+2)+cost[i]
            cache[i] = min(one, two)
            # print(i, cost[i])
            # print(one, two)
            # print(cache)
            return cache[i]

        dfs(0)
        return min(cache[0],cache[1])      
