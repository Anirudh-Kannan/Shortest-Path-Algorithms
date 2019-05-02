from collections import defaultdict
import sys
inf = 999
  


def minimumdist(dist, visited): 
    (mini, minv) = (inf, 0) 
   
    for v in range(len(dist)): 
        if (mini > dist[v] and visited[v] == 0): 
            (mini, minv) = (dist[v], v) 
  
    return minv 
  


  
# Dijkstra Algorithm 
def Dijkstra(G, modifiedGraph, s): 
       
    num = len(G) 
    visit = defaultdict(lambda : False) #this will set default value as false in dictionary
    dist = [inf] * num 
    dist[s] = 0
  
    for count in range(num): 

        cur = minimumdist(dist, visit) 
        visit[cur] = True
  
        for vertex in range(num): 
            if ((visit[vertex] == False) and(dist[vertex] > (dist[cur] + modifiedGraph[cur][vertex])) and (graph[cur][vertex] != 0)): 
                  
                dist[vertex] = (dist[cur] + modifiedGraph[cur][vertex]);
  
    # Print the Shortest distance from the source 
    for vertex in range(num): 
        print ('Vertex ' + str(vertex) + ': ' + str(dist[vertex])) 
  



def BellmanFord(edges, graph, n): 
    dist = [inf] * (n + 1) 
    dist[n] = 0
  
    for i in range(n): 
        edges.append([n, i, 0]) 
  
    for i in range(n): 
        for (s, des, weight) in edges: 
            if((dist[s] != inf) and (dist[s] + weight < dist[des])): 
                dist[des] = dist[s] + weight #relaxation step

    for i in range(len(graph)):         
        
        for j in range(len(graph)):

            temp = dist[j] + graph[j][i]

            if dist[j] == inf:
                temp = inf

            if(temp < dist[i] ):
                print('\nERROR!.....Negative cycle exists')
                sys.exit()
  
    #no need to return added vertex
    return dist[0:n] 
  


# Function to implement Johnson Algorithm 
def JohnsonAlgorithm(G): 
  
    edges = [] 
  
    for i in range(len(G)): 
        for j in range(len(G[i])): 
  
            if G[i][j] != 0: 
                edges.append([i, j, G[i][j]]) 
  
    # Weights used to modify the original weights 
    modifyWeights = BellmanFord(edges, G, len(G)) 
  
    modifiedGraph = [[0 for x in range(len(G))] for y in
                    range(len(G))] 
  
    # Modify the weights to get rid of negative weights 
    for i in range(len(G)): 
        for j in range(len(G[i])): 
  
            if G[i][j] != 0: 
                modifiedGraph[i][j] = (G[i][j] + modifyWeights[i] - modifyWeights[j]); 
  
    print ('Modified Graph: ' + str(modifiedGraph)) 
  
    # Run Dijkstra  
    for source in range(len(G)): 
        print ('\nShortest Distance with vertex ' + str(source) + ' as the source:\n') 
        Dijkstra(graph, modifiedGraph, source) 
  


graph = [[0, 999, 999, 7, 999],  
         [3, 0, 4, 999, 999],  
         [999, 999, 0, 999, 6],  
         [999, 2, 5, 0, 999],
         [999, 999, 999 ,4, 0]
         ] 
  
JohnsonAlgorithm(graph) 