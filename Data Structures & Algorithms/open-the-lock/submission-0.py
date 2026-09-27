class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #input: deadends + target lock
        #output: minimum number of turns to get target or -1

        #have a lock with 4 circular wheels
        #each wheel has 10 slots 0-9, can rotate freely + wrap around like irl lock
        #each movie consists of turning one wheel one slot
    
        #lock starts at 0000
        
        #also get given list of deadends meaning if lock is any of those codes, it stops turning

        #constraints:
        #can have like 500 deadends
        #everything is 4 long
        #target isnt a deadend - so could 0000 be a deadend?
        #only digits

        #bfs
        #meaning we need queue + visited
        #visited will start off as deadends
        #queue will track values like [curr lock, turns]
        #half backtracking half bfs where we just +- 1 each digit and add to queue if not seen
        #if we match the target just return the turns, if we go through every combo then -1
        #bfs is -> queue + pop queue + iterate thru "neighbors" + add to queue and visited if not in

        #how to get +-1 of each digit:
        #for each digit
        #if ++, then just mod 10
        #if --, then add 10 then mod 10
        #need to get all 8 options for that lock

        from collections import deque

        if '0000' in deadends:
            return -1

        def locks(curr):
            locks = []
            for i in range(4):
                digit = (int(curr[i])+1)%10
                plus = curr[:i]+str(digit)+curr[i+1:]
                locks.append(plus)
                digit = (int(curr[i])-1+10)%10
                minus = curr[:i]+str(digit)+curr[i+1:]
                locks.append(minus)

            return locks

        visited, queue = set(deadends), deque([['0000', 0]])

        while queue:
            curr_lock, curr_turns = queue.popleft()

            if curr_lock == target:
                return curr_turns
            
            for lock in locks(curr_lock):
                if lock not in visited:
                    visited.add(lock)
                    queue.append([lock, curr_turns+1])
            


        return -1

        
        