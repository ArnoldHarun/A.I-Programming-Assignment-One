
graph = {'S': ['A', 'B'],
         'A': ['B', 'C'],
         'C': ['D', 'G'],
         'B': ['C'],
         'D': ['G']}
print('****Visited Nodes in Order****')

#   Breadth First(uses Queue)
def BFS(graph,start,goal):
    visited=[]
    queue=[[start]]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        print(visited)
        if node==goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path=path.copy()
                new_path.append(node2)
                queue.append(new_path)
    
solution=BFS(graph,'S','G')
print("*****Path for BFS****")
print(solution)