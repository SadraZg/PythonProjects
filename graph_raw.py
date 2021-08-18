import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


class Graph:

    def __init__(self, a):
        self.adj_list = a
        self.adj_matrix = nx.from_numpy_matrix(self.adj_list)
        self.node_count = len(self.adj_list)
        self.edge_count = 0


def draw_matrix(mat):

    nx.draw(nx.from_numpy_matrix(mat), with_labels=1)
    plt.show()


def node_edge_process():

    global edges, node_neighbor
    double_edge_count = 0
    edges = {}
    node_neighbor = {}
    for i in range(A.node_count):
        for j in range(A.node_count):
            if A.adj_list[i][j] == 1:
                double_edge_count += 1
                edge = tuple(sorted([i, j]))
                if i in node_neighbor.keys():
                    node_neighbor[i].append(j)
                else:
                    node_neighbor[i] = [j]
                if edge not in edges.values():
                    edges[len(edges)] = edge

    A.edge_count = int(double_edge_count / 2)
    # print("edges: ", edges)
    # print("neighbors: ", node_neighbor)


def incidence():

    print("\n############################# Incidence matrix ##########################")

    inc_matrix = []
    for i in range(A.node_count):
        inc_matrix.append(A.edge_count * [0])

    for i in range(A.node_count):
        for j in range(A.edge_count):
            if edges[j][0] == i or edges[j][1] == i:
                inc_matrix[i][j] = 1
            else:
                inc_matrix[i][j] = 0

    # Print the incidence matrix
    for i in inc_matrix:
        print(i)
    return True


def is_connected():

    print("\n######################## Is the graph connected? ########################")

    flag = True
    checking = deepcopy(matrix)
    for i in range(2, A.node_count+1):
        step = np.linalg.matrix_power(matrix, i)
        checking += step

    for row in checking:
        for item in row:
            if item == 0:
                flag = False
    if not flag:
        print("No, it's not connected")
    else:
        print("Yes, it's connected")


def is_cyclic(v, visited, parent):

    # Mark current node as visited
    visited[v] = True

    for neighbor in node_neighbor[v]:

        if not visited[neighbor]:
            if is_cyclic(neighbor, visited, v):
                return True

        elif neighbor != parent:
            return True

    return False


def is_tree():

    print("\n########################### Is graph a tree? ############################")

    visited = [False] * A.node_count

    if is_cyclic(0, visited, -1):
        print("No, it's not a tree")
        return False

    for i in range(A.node_count):
        if not visited[i]:
            print("No, it's not a tree")
            return False

    print("Yes, it's a tree")
    return True


def degree_determination():

    print("\n################### What is the degree of each node? ####################")

    global node_degree

    node_degree = {}
    for node, neighbors in node_neighbor.items():
        node_degree[node] = len(neighbors)

    print(node_degree)


def max_degree():

    print("\n#################### Which node has the most degree? ####################")

    max_deg = max(node_degree.values())

    for node, degree in node_degree.items():
        if degree == max_deg:
            print("Node {} has the most degree = {}".format(node, max_deg))
            return True


def minimum_spanning_tree():

    print("\n######################### Minimum spanning tree #########################")

    visited = [False] * A.node_count
    queue = [0]                             # source
    spanning = deepcopy(matrix)             # replica of our matrix. we will delete some edges of it
    passed_nodes = []

    while len(queue) != 0:
        now = queue[0]
        visited[now] = True
        queue.remove(queue[0])

        for neighbor in node_neighbor[now]:
            if neighbor not in passed_nodes:
                if not visited[neighbor] and neighbor not in queue:
                    queue.append(neighbor)
                else:
                    spanning[now][neighbor] = 0
                    spanning[neighbor][now] = 0

        passed_nodes.append(now)

    print(spanning)


def bfs(src, dest, pred, dist):

    visited = [False] * A.node_count

    queue = []

    for i in range(A.node_count):
        dist[i] = 1000000
        pred[i] = -1

    visited[src] = True
    dist[src] = 0
    queue.append(src)

    # BFS algorithm
    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)

        for i in range(len(node_neighbor[u])):

            if not visited[node_neighbor[u][i]]:
                visited[node_neighbor[u][i]] = True
                dist[node_neighbor[u][i]] = dist[u] + 1
                pred[node_neighbor[u][i]] = u
                queue.append(node_neighbor[u][i])

                # Stop BFS when we find destination
                if node_neighbor[u][i] == dest:
                    return True

    return False


def shortest_path(s, dest):

    print("\n############### what is the shortest path between {} and {} ###############".format(s, dest))

    # predecessor[i] array stores predecessor of i
    # distance array stores distance of i from s
    pred = [0] * A.node_count
    dist = [0] * A.node_count

    if not bfs(s, dest, pred, dist):
        print("Given source and destination are not connected")

    # vector path stores the shortest path
    path = []
    crawl = dest
    path.append(crawl)

    while pred[crawl] != -1:
        path.append(pred[crawl])
        crawl = pred[crawl]

    # distance from source is in distance array
    print("Shortest path length is: ", dist[dest])

    # printing path from source to destination
    print("Path is: ", end=' ')
    for i in range(len(path) - 1, -1, -1):
        if i != 0:
            print(path[i], end=' -> ')
        else:
            print(path[i])


def is_safe(node, colors, node_color):

    for i in range(A.node_count):
        if matrix[node][i] == 1 and colors[i] == node_color:
            return False
    return True


def graph_color_util(number_of_colors, colors, node):

    if node == A.node_count:
        return True
    for c in range(1, number_of_colors + 1):
        if is_safe(node, colors, c):
            colors[node] = c
            if graph_color_util(number_of_colors, colors, node + 1):
                return True
            colors[node] = 0


def graph_coloring(number_of_colors):

    colors = [0] * A.node_count

    if graph_color_util(number_of_colors, colors, 0) is None:
        return False

    return colors


def coloring():

    print("\n####### Color the graph with the least number of colors possible ########")

    node_color = {}
    for i in range(2, A.node_count+1):
        if not graph_coloring(i):
            continue
        else:
            # Print the solution
            for c in range(len(graph_coloring(i))):
                node_color[c] = graph_coloring(i)[c]
            print(node_color)
            return True


def is_bipartite():

    print("\n######################## Is the graph bipartite? ########################")

    if graph_coloring(2):
        print("The graph is bipartite")
    else:
        print("The graph is not bipartite")


# matrix = np.array([[0, 1, 1, 0, 0],
#                    [1, 0, 1, 0, 1],
#                    [1, 1, 0, 1, 1],
#                    [0, 0, 1, 0, 0],
#                    [0, 1, 1, 0, 0]])

# matrix = np.array([[0, 1, 1, 0, 0],
#                    [1, 0, 0, 0, 0],
#                    [1, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 1],
#                    [0, 0, 0, 1, 0]])

# matrix = np.array([[0, 1, 1, 0],
#                    [1, 0, 0, 0],
#                    [1, 0, 0, 1],
#                    [0, 0, 1, 0]])

matrix = np.array([[0, 1, 0, 1, 0, 1, 1],
                   [1, 0, 1, 0, 0, 1, 1],
                   [0, 1, 0, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1],
                   [0, 0, 1, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 0, 1, 0]])

# matrix = np.array([[0, 1, 0, 1],
#                    [1, 0, 1, 0],
#                    [0, 1, 0, 1],
#                    [1, 0, 1, 0]])

A = Graph(matrix)
# draw_matrix(matrix)
node_edge_process()
incidence()
is_connected()
is_tree()
degree_determination()
max_degree()
minimum_spanning_tree()
# draw_matrix(B)
shortest_path(0, 3)
coloring()
is_bipartite()
