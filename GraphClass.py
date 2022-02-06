# Create a class that converts a dictionary of vertices and costs into an organized Graph object.
class Graph:
    def __init__(self, table: dict):
        """Create a Graph object"""
        self.table = table

    def get_branches_from(self, letter):
        """Obtain all the vertices connected to a given node/vertex,"""
        branches = {}
        try:
            first_branch = self.table[letter]
        except KeyError:
            raise Exception(f"\"{letter}\" DNE") from None
        branches.update(first_branch)

        for key, dictionary in self.table.items():
            if key != letter:
                if letter in dictionary.keys():
                    branches.update({key: dictionary[letter]})
        return branches

    def get_vertices(self):
        """Grab all the vertices of a Graph."""
        return tuple(self.table.keys())
