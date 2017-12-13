import networkx as nx

f = open("input.txt", "r")
lines = f.readlines()

# lines = ["0 <-> 2",
#          "1 <-> 1",
#          "2 <-> 0, 3, 4",
#          "3 <-> 2, 4",
#          "4 <-> 2, 3, 6",
#          "5 <-> 6",
#          "6 <-> 4, 5"]

g = nx.Graph()

for line in lines:
    node, connections = line.split("<->")
    node = int(node)
    connections = connections.split(",")
    connections = [int(i) for i in connections]

    g.add_node(node)
    for connection in connections:
        g.add_edge(node, connection)

graphs = list(nx.connected_component_subgraphs(g))


for graph in graphs:
    if 0 in graph:
        print("Solution 1: {0}".format(len(graph)))
        break

print("Solution 2: {0}".format(len(graphs)))