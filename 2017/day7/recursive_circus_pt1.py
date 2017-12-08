import networkx as nx

f = open("input.txt", "r")
lines = f.readlines()

graph = nx.DiGraph()

for line in lines:
    name = line.split()[0]

    graph.add_node(name, weight=int(line.split()[1].strip('()')))

    if '->' in line:
        children = [n.strip() for n in line.split('->')[1].split(',')]

        for child in children:
            graph.add_edge(name, child)

ordered = list(nx.topological_sort(graph))
print("Solution: {0}".format(ordered[0]))