import heapq


class Graph(object):
    def __init__(self, nodes):
        self.edges = [[] for i in range(nodes)]

    def add(self, source, length, destination):
        self.edges[source].append((length, destination))
        pass


def dijkstra(graph, start, nodes):
    D = [100000 for v in range(nodes)]
    D[start] = 0

    pq = [(0, start)]

    while len(pq) > 0:
        current_distance, node = heapq.heappop(pq)
        if current_distance > D[node]:
            continue

        for weight, neighbor in graph.edges[node]:
            distance = current_distance + weight

            if distance < D[neighbor]:
                D[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return D


n, m, q = str(input()).split()
q, m, n = int(q), int(m), int(n)
graph = Graph(n)
for i in range(m):
    u, v, l = str(input()).split()
    l, v, u = int(l), int(v), int(u)
    if u != v:
        graph.add(u, l, v)
        graph.add(v, l, u)

remember = ['' for sxda in range(n)]
for i in range(q):
    p = int(input())
    if remember[p] != '':
        print(remember[p])
    else:
        dist = dijkstra(graph, p, n)
        dist.sort()
        d = []
        for y in dist:
            if y != 100000 and y != 0:
                d.append(y)

        if len(d) == 0:
            res = '(' + str(p) + ', 0, 1)'
            print(res)
            remember[p] = res
        else:
            count = 0
            for dd in d:
                if dd == max(d):
                    count += 1
            res = '(' + str(p) + ', ' + str(max(d)) + ', ' + str(count) + ')'
            print(res)
            remember[p] = res
