class Node:
    ### Node in a graph ###
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
    
    def __str__(self):
        return "NODE -> Name: " + self.name + ", Heuristic: " + str(self.heuristic)
    
class Connection:
    ### Connection between 2 nodes in a graph ###
    def __init__(self, parent_node, child_node, cost):
        self.parent_node = parent_node
        self.child_node = child_node
        self.cost = cost
    
    def __str__(self):
        return "NODES -> From: " + self.parent_node.name + ", To: " + self.child_node.name + ", Cost: " + str(self.cost)

class Graph:
    ### A graph (collection of nodes) ###
    def __init__(self):
        self.nodes = list()
        self.connections = list()
    
    def add_node(self, node_to_add):
        self.nodes.append(node_to_add)
    
    def add_connection(self, parent_node, child_node, cost):
        self.connections.append(
            Connection(parent_node, child_node, cost)
        )
    
    def is_connection_present(self, parent_node, child_node):
        for connection in self.connections:
            if (connection.parent_node == parent_node and
                connection.child_node == child_node):
                return True
        return False
    
    def get_connection_cost(self, parent_node, child_node):
        for connection in self.connections:
            if (connection.parent_node == parent_node and
                connection.child_node == child_node):
                return connection.cost
        return None

    def get_all_connections(self, node):
        list_of_connections = list()
        for connection in self.connections:
            if (connection.parent_node.name == node.name):
                list_of_connections.append(connection)
        return list_of_connections

    def __str__(self):
        graph_as_string = "\n"
        for connection in self.connections:
            graph_as_string += str(connection) + "\n"
        return graph_as_string   
    
S = Node('S', 7)
A = Node('A', 5)
B = Node('B', 7)
C = Node('C', 4)
D = Node('D', 1)
G = Node('G', 0)

graph = Graph()
graph.add_node(S)
graph.add_node(A)
graph.add_node(B)
graph.add_node(C)
graph.add_node(D)
graph.add_node(G)

graph.add_connection(S, A, 3)
graph.add_connection(S, B, 1)
graph.add_connection(A, B, 2)
graph.add_connection(A, C, 2)
graph.add_connection(C, D, 4)
graph.add_connection(C, G, 4)
graph.add_connection(B, C, 3)
graph.add_connection(D, G, 1)
print('****Graph showing Nodes and Connection****')
print(graph)

path_of_GREEDY = []

def GREEDY(start_node, goal_node):
    frontier_list = list()
    
    current_node = start_node
    is_goal_found = False
    
    while(not is_goal_found):
        if current_node not in path_of_GREEDY:
            path_of_GREEDY.append(current_node)

        if current_node.name == goal_node.name:
            return goal_node
        
        for connection in graph.get_all_connections(current_node):
            if connection.child_node not in frontier_list:
                frontier_list.append(connection.child_node)
        
        smallest_heuristic_node = frontier_list[0]
        for node in frontier_list[1:]:
            if (node.heuristic < smallest_heuristic_node.heuristic):
                smallest_heuristic_node = node
        current_node = smallest_heuristic_node
        
GREEDY(S, G)

print('****Total Cost of Greedy Search and Path****')

cost_of_GREEDY = 0
for index, node in enumerate(path_of_GREEDY[:-1]):
    cost_of_GREEDY += graph.get_connection_cost(node, path_of_GREEDY[index+1])
    print(node)
print("Total cost of GREEDY Search is : ", cost_of_GREEDY)