class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #input: 2d array of 0(empty) 1(fresh) 2(rotten)
        #output: minimum number of minutes to rot all fruit, if not possible then -1

        #constraints:
        #at least 1x1 grid

        #fruit can become rotten if top below right or left or normal fruit

        #going to use bfs
        #need to bfs since it's we need to track minutes

        #need a double for loop to find all rotten locations + fresh fruit number
        #need bfs starting at rotten fruit queue and until queue empty

        #for i in range
        #   for j in range
        #       if 1 increment number, if 2 add coord to queue

        #while we have a queue
        #   for each item in the queue rn
        #       make it a rotten fruit
        #       for up, down, left, right: add to queue if 1 and not seen, and not out of bound
        #           if we add to queue, then add to visited so we dont double dip
        #increment answer by 1

        from collections import deque

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        queue = deque()
        visited = set()
        answer = 0
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh+=1

        while queue and fresh > 0:
            loops = len(queue)
            for i in range(loops):
                curri, currj = queue.popleft()
                for diri, dirj in directions:
                    tempi, tempj = curri+diri, currj+dirj
                    if tempi < 0 or tempj < 0 or tempi > len(grid)-1 or tempj > len(grid[0])-1 or grid[tempi][tempj] != 1 or (tempi,tempj) in visited:
                        continue
                    queue.append((tempi, tempj))
                    visited.add((tempi,tempj))
                    grid[tempi][tempj] = 2
                    fresh-=1
            answer+=1

        return answer if fresh < 1 else -1




