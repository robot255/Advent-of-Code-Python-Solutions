import networkx as nx


f = open("input.txt", "r")
lines = f.readlines()


graph = nx.DiGraph()

# Build the graph of programs
for line in lines:
    name = line.split()[0]

    graph.add_node(name, weight=int(line.split()[1].strip('()')))

    if '->' in line:
        children = [n.strip() for n in line.split('->')[1].split(',')]

        for child in children:
            graph.add_edge(name, child)

# Topological sort to find the root of the tree
ordered = list(nx.topological_sort(graph))

# Keep track of each node's total weight (itself + its children)
weights = {}

for node in reversed(ordered):
    total = graph.nodes[node]['weight']

    val = None
    unbalanced = None

    for child in graph[node]:
        if val is not None and weights[child] != val:
            unbalanced = child
            break

        # Otherwise add to the total weight
        val = weights[child]
        total += weights[child]

    if unbalanced:
        # Find the weight adjustment and the new weight of this node
        diff = abs(val - weights[unbalanced])
        print('Solution:', graph.nodes[unbalanced]['weight'] - diff)
        break

    # Store the total weight of the node
    weights[node] = total