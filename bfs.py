inf = 0

def bfs(G,n,v,s):
    v[s] = 1
    q = list()
    q.append(s)
    parent = {s:None}
    dist={s:0}

    while(q):
        node = q.pop()
        for i in range(n):
            if(G[node][i]!=inf and v[i] == 0):
                v[i] = 1
                parent[i] = node
                dist[i] = dist[node] + G[node][i]
                q.append(i)

    return (parent,dist)


print("Shortest path using BFS Algorithm")

n = int(input('Enter the number of vertices in the graph: '))

print('\nEnter the Cost Matrix:')
G = [[int(x) for x in input().split()] for i in range(0,n)]

s = int(input('Enter the source vertex number(starting from 0): '))

v = list()

for i in range(n):
    v.append(0)

(parent,distance) = bfs(G,n,v,s)

print("Node Cost")


for (key1, value1) in distance.items() :
    print(key1,value1)

print("Node Parent")
for (key1, value1) in parent.items():
    print(key1, value1)
