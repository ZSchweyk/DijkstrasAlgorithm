class Node:
    names = {}

    def __init__(self, name):
        if name not in self.names.keys():
            self.names[name] = self
            self.name = name
            self.branches = {}
        else:
            raise Exception(f"\"{name}\" already exists.")

    def cost_to(self, node, cost: float):
        if isinstance(node, Node):
            self.branches[node] = cost
            node.branches[self] = cost
        elif isinstance(node, str):
            self.branches[self.names[node]] = cost
            self.names[node].branches[self] = cost

    def get_branches(self):
        return self.branches

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self, nodes: list[Node]):
        self.nodes = {node.name: node for node in nodes}

    def get_branches_from(self, node_name: str):
        try:
            return {node_obj.name: cost for node_obj, cost in self.nodes[node_name].get_branches().items()}
        except KeyError:
            raise Exception(f"\"{node_name}\" DNE in the nodes, {self.nodes}, of this Graph object.")


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
print(graph.get_branches_from("E"))
