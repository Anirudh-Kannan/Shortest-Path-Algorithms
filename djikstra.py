inf = 999


def dijkstra(g,n):
    k=int(input("Enter the source vertex: "))
    visited = []
    visited.append(k)
    pos=0
    cost = [0 for x in range(n)]
    
    for j in range(n):
        cost[j]=g[k][j]
    les=inf

    for x in range (n-1):
        les=inf
        for j in range (n):
                if (cost[j]<=les and j not in visited):
                        les=cost[j]
                        pos=j
        visited.append(pos)


        for j in range (n):
            if (cost[j] >cost[pos]+g[pos][j]):#update cost of all vertices from source
                cost[j]=cost[pos]+g[pos][j]


    print("The shortest path is:\n")
    print("Visited\tCost")
    for i in range(1,len(visited)):              
            print(visited[i],cost[i])



print("Djikstra's Algorithm")

n = int(input('Enter the number of vertices in the graph: '))

print('\nEnter the Cost Matrix:')
G = [[int(x) for x in input().split()] for i in range(0,n)]


dijkstra(G,n)


