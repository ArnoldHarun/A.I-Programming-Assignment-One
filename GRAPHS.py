# Directed Graph
graph ={  'S':['A','B'],
          'A':['B','C'],
          'B':['C'],
          'C':['D','G'],
          'D':['G'],
          'G':set()
          }
          
          

# Weighted Graph with costs
#   ....**NODE:COST**....

graph = {'S':{'A':3, 'B':1},
         'A':{'B':2, 'C':2},
         'C':{'D':4, 'G':4},
         'B':{'C':3},
         'D':{'G':1}   
        }