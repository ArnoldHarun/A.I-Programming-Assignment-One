Graph = {'A':{'B':2,'C':2},
     'B':{'C':3,},
     'C':{'G':4,'D':4},
     'G':{},
     'S':{'B':1,'A':3},
     'D':{'G':1}
     }
#Depth First(uses Stack)
class DFS:
    def DFS_Path(self, graph, source_node, goal_node):
        visited,stack = set(),[[source_node]]

        while stack:
            path = stack.pop()
            node = path[-1]

            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    new_path = path + [neighbor]
                    stack.append(new_path)

            if node == goal_node:
                return path
        return None
dfs = DFS()
#                         Modules:     'Source' , 'Destination'
DFS_Path = dfs.DFS_Path(Graph, 'S', 'G')
print("\nThe shortest path using DFS is   =", DFS_Path)