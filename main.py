from NodeClass import Node
from GraphClass import Graph

# Adjusted the Node and Graph class to account for repetitive table inputs correctly.

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

a.cost_to(b, 5)
a.cost_to(c, 2)

b.cost_to(c, 2)
b.cost_to(e, 1)
b.cost_to(d, 4)

c.cost_to(e, 5)

d.cost_to(e, 5)
d.cost_to(f, 2)
d.cost_to(g, 3)

e.cost_to(f, 7)

f.cost_to(g, 1)

graph = Graph([a, b, c, d, e, f, g])
print(graph.shortest_path("F", "G"))
