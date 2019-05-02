import sys


inf = 999
NULL = 'NULL'




def bellmanford(G, S):
#initialise the lists containing the distance and previous node
    distance = list()
    previous = list()


#make all distances infinity initially and set source distance to 0
    for i in range(len(G)):
        distance.append(inf)
        previous.append(NULL)
        

    distance[S] = 0
    

#edges are now going to be relaxed
    for k in range(len(G)-1):
        for i in range(len(G)):         #loop over each vertex in G
            
            for j in range(len(G)):  #loop over each vertex neighbouring vertex i
                
                temp = distance[j] + G[j][i]

                if distance[j] == inf:
                    temp = inf
                
                if(temp < distance[i]):
                    distance[i] = temp
                    previous[i] = j
                    

#check for negative cycle

    for i in range(len(G)):         
        
        for j in range(len(G)):

            temp = distance[j] + G[j][i]

            if distance[j] == inf:
                temp = inf

            if(temp < distance[i] ):
                print('\nERROR!.....Negative cycle exists')
                sys.exit()

    return (distance,previous)





print("Bellman Ford Algorithm")

n = int(input('Enter the number of vertices in the graph: '))

print('\nEnter the Cost Matrix:')
G = [[int(x) for x in input().split()] for i in range(0,n)]

S = int(input('Enter the source vertex number(starting from 0): '))
(distance, previous) = bellmanford(G,S)

print('Vertex:\tDistance:')

for i in range(n):
    print(str(i)+'\t'+str(distance[i]))


