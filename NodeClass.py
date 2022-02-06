class Node:
    def __init__(self, name):
        self.name = name
        self.branches = {}

    def cost_to(self, node_obj, cost: float):
        self.branches[node_obj] = cost
        node_obj.branches[self] = cost

    def get_branches(self):
        return self.branches

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self, nodes: list):
        self.nodes = nodes



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

print(d.get_branches())
