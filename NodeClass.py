class Node:
    names = {}
    bi_directional = False

    def __init__(self, name):
        """
        Constructor.
        Make sure that the name parameter is unique. If not, throw an exception.
        """
        if name not in self.names.keys():
            self.names[name] = self
            self.name = name
            self.branches = {}
        else:
            raise Exception(f"\"{name}\" already exists.")

    def cost_to(self, node, cost: float):
        """Accepts the node object or node.name as node, and modifies the branch of self accordingly."""
        if isinstance(node, Node):
            self.branches[node] = cost
            if self.bi_directional: node.branches[self] = cost
        elif isinstance(node, str):
            self.branches[self.names[node]] = cost
            if self.bi_directional: self.names[node].branches[self] = cost

    def get_branches(self):
        """Get the branches of a node."""
        return self.branches

    def __repr__(self):
        """I added this so that printing out objects would look nicer."""
        return self.name
