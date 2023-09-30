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

def shortest_path(u, v, selected = []):
    if v == u:
        return selected
    
    selected.append(u)
    
    min_edge = 10000
    min_node = ""

    for connection in graph.get_all_connections(u):
        
        if (connection.child_node.name == v.name):
            selected.append(connection.child_node)
            return selected

        if (graph.get_connection_cost(u, connection.child_node) < min_edge) and not(connection.child_node in selected):
            min_edge = graph.get_connection_cost(u, connection.child_node)
            min_node = connection.child_node
            shortest_path(min_node, v, selected)

def UCS(S, G):
    list_of_outputs = []
    shortest_path(S, G, list_of_outputs)
    
    total_cost = 0
    for index, node in enumerate(list_of_outputs[:-1]):
        cost = graph.get_connection_cost(node, list_of_outputs[index+1])
        if (cost is not None):
            total_cost += cost
        print("From: ", node.name, "\tTo:", list_of_outputs[index+1].name, "\t\tCost:", cost)

    print("Total cost from ", S.name, " to ", G.name, " is", total_cost)
  
print('****Total cost and Path of Nodes****')  
UCS(S, G)