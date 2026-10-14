class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #input: list of locks we cant have, and target lock. also start at 0000
        #output: need to return min number of turns to get target, or -1 if impossible

        #general
        #lock with 4 wheels(0-9 is numbers on each wheel), since wheel, it can wrap around, so 9-0 or 0-9
        #we start at 0000
        #given a list of codes that we cant traverse across or onto, will break

        #constraints + edge cases
        #will have at least one deadend, lock will always be 4 long
        #target isnt a deadlock, but target isnt guaranteed to be found
        
        #cant always find the target
        #should consider wrapping around
        #0000 could be a deadend, so brick before start

        #tests + examples
        

        #solve in english
        #at each step, we have a decision tree. at each digit, up or down, meaning 8 choices per step
        #solve using bfs -> need queue + set(deadends)
        #pop item from the queue [1234, 10]
        #some base op, checking if we have target
        #append neighbors from decision tree, if not visited, add to queue
        #if we run out of places to visit, just exit

        #for each digit in the code
        #do a +-1 and remake the code, return all 8 possibilities
        #if ++ just mod 10
        #if -- just add 10 and then mod 10

        #solve in psuedo
        #queue, visited = deque([0000]), set(deadends)
        #while queue:
        #   queue.pop and check if we have num, if so reutrn the turns
        #   
        #   for each neighbor in curr:
        #       if not in visited add to queue and add to visited, otw skip

        def neighbors(curr):
            children = []
            for i in range(4):
                inc = curr[:i]+str((int(curr[i])+1)%10)+curr[i+1:]
                children.append(inc)
                dec = curr[:i]+str((int(curr[i])-1+10)%10)+curr[i+1:]
                children.append(dec)
            return children


        queue, visited = deque([['0000', 0]]) if '0000' not in deadends else deque([]), set(deadends)
        while queue:
            curr, turns = queue.popleft() #[lock, turns]
            if curr == target:
                return turns

            for neighbor in neighbors(curr):
                if neighbor not in visited:
                    queue.append([neighbor, turns+1])
                    visited.add(neighbor)

        return -1
