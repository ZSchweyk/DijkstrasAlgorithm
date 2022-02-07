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
h = Node("H")
i = Node("I")

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





a.cost_to(b, 5)
a.cost_to(c, 2)

b.cost_to(c, 2)
b.cost_to(e, 1)
b.cost_to(d, 4)
b.cost_to(a, 5)

c.cost_to(e, 5)
c.cost_to(b, 2)
c.cost_to(a, 2)

d.cost_to(e, 5)
d.cost_to(f, 2)
d.cost_to(g, 3)
d.cost_to(b, 4)

e.cost_to(f, 7)
e.cost_to(d, 5)
e.cost_to(b, 1)
e.cost_to(c, 5)

f.cost_to(g, 1)
f.cost_to(d, 2)
f.cost_to(e, 7)


graph = Graph([a, b, c, d, e, f, g, h, i])
print(graph.shortest_path("A", "G"))
print(graph.longest_path("A", "G"))

