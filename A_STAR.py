
# A* Search
# f(n) = g(n) + h(n)
# where n is a node, g(n) is the distance from start to n
# and h(n) is the estimated distance to the end from n
# to each graph

#import operator
from heapq import heappush as push
from heapq import heappop as pop

class Node:
     def __init__(self, n, g, heurs):
          self.parent = None
          self.name = n           
          self.g = g              
          self.h = heurs[n]       
     
     def f(self):
          return self.g + self.h

     def __lt__(self, other):
          return self.f() < other.f()




# Graph and Connection  S -> G
G = {'A':{'B':2,'C':2},
     'B':{'C':3,},
     'C':{'G':4,'D':4},
     'G':{},
     'S':{'B':1,'A':3},
     'D':{'G':1}
     }

H = {'S':7,'A':5,'B':7,'C':4,'D':1,'G':0}


#Finds the shortest path to target from source
def solve(source, target, graph, heurs):

     open_heap = [] # nodes left to search
     closed_list = [] # searched nodes

     first_node = Node(source, 0, heurs)

     push(open_heap, first_node) # add it to the open_heap

     while open_heap: # while the heap is not empty

          # create the current working node and remove from open
          current_node = open_heap[0]
          pop(open_heap)

          # if we reach the end node, we are done
          if current_node.name == target:
               return get_path(current_node)

          # check the entire list of nodes adjacent to the current node
          for next in list(graph[current_node.name].keys()):

               curr_cost = current_node.g + graph[current_node.name][next] # cost to get to current node
               next_node = Node(next, graph[current_node.name][next], heurs) # new node of the next in adjacency

               # if the node is unopened, and next's g is lower than current g
               if next_node in open_heap and next_node.g <= curr_cost:
                    pass # just skip to next iteration
               elif next_node in closed_list: # if its closed
                    if next_node.g <= curr_cost: # and the g is less than current g
                         pass # skip to next iteration
                    closed_list.remove(next_node) # then reopen the node
                    push(open_heap, next_node) # adding it to the open heap again
               else: # just add it to the open list
                    push(open_heap, next_node)
               
               # Move on to the next adjacent node
               next_node.g = curr_cost
               next_node.parent = current_node

          # add to the closed list once it has been fully searched
          closed_list.append(current_node)

# function to retrace the steps
# and also properly format into readable print
def get_path(node):

     path = []

     while node:
          path.insert(0, (node.g, node.name))
          node = node.parent

     print('')
     # Printing the shortest path, final g-cost is the total
     for i in range(0, len(path)):
          if path[i] != path[-1]:
               print(str(path[i][1]), end=' -> ')
          else:
               print(str(path[i][1]))
               print("Total Distance => " + str(path[i][0]))
     print('')

if __name__=="__main__":
    
     source = 'S'
     target = 'G'
     print('**Path and Total Cost for A* Search****')
     solve(source, target, G, H)

    