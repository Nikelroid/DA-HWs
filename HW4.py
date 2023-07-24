def reconstruct_graph(shortest_paths):
    num_nodes = len(shortest_paths)
    edges = 0
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            is_direct_edge = True
            for k in range(num_nodes):
                if k == i or k == j:
                    continue
                if shortest_paths[i][j] == shortest_paths[i][k] + shortest_paths[k][j]:
                    is_direct_edge = False
                    break
            if is_direct_edge:
                edges += 1
    return edges

def is_valid_graph(shortest_paths):
    num_nodes = len(shortest_paths)
    for i in range(num_nodes):
        if shortest_paths[i][i] != 0:
            return False
    for i in range(num_nodes):
        for j in range(num_nodes):
            if shortest_paths[i][j] != shortest_paths[j][i]:
                return False
    for i in range(num_nodes):
        for j in range(num_nodes):
            for k in range(num_nodes):
                if shortest_paths[i][j] > shortest_paths[i][k] + shortest_paths[k][j]:
                    return False
    return True

d = []
num_nodes = int(input())
for i in range(num_nodes):
    d.append([])
    d[-1] = list(map(int, str(input()).split(" ")))

if is_valid_graph(d):
    print(reconstruct_graph(d))
else:
    print(-1)
