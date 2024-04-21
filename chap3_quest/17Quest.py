import itertools

def tsp_brute_force(graph):
    n = len(graph)
    
    all_pm = itertools.permutations(range(1, n))
    
    Mcost = float('inf')
    Mpath = None
    
    for k in all_pm:

        cost = graph[0][k[0]] 
        
        for i in range(len(k) - 1):
            cost += graph[k[i]][k[i + 1]]
        

        cost += graph[k[-1]][0]
        

        if cost < Mcost:
            Mcost = cost
            Mpath = (0,) + k + (0,)
    
    return Mpath, Mcost

graph = [
    [0, 20, 35, 15],
    [10, 0, 20, 25],
    [15, 35, 0, 30],
    [20, 15, 30, 0]
]
Mpath, Mcost = tsp_brute_force(graph)
print("최단 경로:", Mpath)
print("최소 비용:", Mcost)