class Graph:
    def __init__(self, table: dict):
        self.table = table

    def get_branches_from(self, letter):
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
        return tuple(self.table.keys())

def shortest_path(graph: Graph, start, finish):
    table = []
    for vertex in graph.get_vertices():
        table.append([vertex, 0 if vertex == start else float("inf"), ""])
    processed = []
    vertex_to_process = min(table, key=lambda row: row[1])[0]
    while vertex_to_process != finish:
        branches = {vertex: cost for vertex, cost in graph.get_branches_from(vertex_to_process).items() if vertex not in processed}
        print(branches)

        break





table = {
    "A": {"B": 5, "C": 2},
    "B": {"C": 2, "E": 1, "D": 4},
    "C": {"E": 5},
    "D": {"E": 5, "G": 3, "F": 2},
    "E": {"F": 7},
    "F": {"G": 1},
    "G": {}
}

g = Graph(table)
shortest_path(g, "A", "G")





