class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #input: int n and edges [a,b]
        #output: number of connected comp in graph

        #undirected graph of n nodes from 0 -> n-1
        
        #constraints:
        #have at least 1 node and thus 1 edge
        #no self edges or repeated edges

        #build adj list of the given edges
        #then start a bfs thing to traverse through it and count each time we start bfs

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        #so gonna loop through adj list
        #start bfs at somewhere we havent visited yet
        #just bfs and add all neighbors in until we're good
        answer = 0
        visited, queue = set(), deque() 
        for i in range(len(adj_list)):
            if i not in visited:
                queue.append(i)

                while queue:
                    curr = queue.popleft()

                    for neighbor in adj_list[curr]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)

                answer+=1
        
        return answer
                
        
        