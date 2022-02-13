from NodeClass import Node
from GraphClass import Graph

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

Node.bi_directional = True

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

# Islands [a, b, c], [d, e, f], [g], [h], [i]
# a.cost_to(b, 5)
# a.cost_to(c, 2)
# c.cost_to(a, 2)
# c.cost_to(b, 2)
# b.cost_to(a, 5)
# b.cost_to(c, 2)
#
# e.cost_to(d, 5)
# e.cost_to(f, 7)
# f.cost_to(e, 7)
# f.cost_to(d, 2)
# d.cost_to(e, 5)
# d.cost_to(f, 2)

graph = Graph([a, b, c, d, e, f, g])
print(graph.shortest_path("A", "G"))

