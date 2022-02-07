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