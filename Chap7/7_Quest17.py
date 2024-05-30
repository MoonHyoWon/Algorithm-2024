import copy
def shortest_path_floyd(vertex, W):
    vsize = len(vertex)
    D = copy.deepcopy(W)

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if(D[i][k] + D[k][j] < D[i][j]):
                    D[i][j] = D[i][k] + D[k][j]
            printD(D)

def printD(D):
    vsize = len(D)
    print("================================================")
    for i in range(vsize):
        for j in range(vsize):
            if(D[i][j] == INF): print("INF ", end="")
            else : print("%3d " % D[i][j], end="")
        print("")

INF = 9999
vertex = [ 'A', 'B', 'C', 'D', 'E', 'F']
weight = [[ 0, 7, 9, INF, INF, 14 ],
          [ 7, 0, 10, 15, INF, INF],
          [ 9, 10, 0, 11, INF, INF],
          [ INF, 15, 11, 0, 6, INF],
          [ INF, INF, INF, 6, 0, 9],
          [ 14, INF, INF, INF, 9, 0]]


print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vertex, weight)