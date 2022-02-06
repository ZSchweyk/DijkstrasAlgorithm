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

def shortest_path(graph: Graph, start_vertex, end_vertex):
    table = {}
    for vertex in graph.get_vertices():
        table.update({vertex: [0 if vertex == start_vertex else float("inf"), ""]})
    print(table)

    processed = []
    calculate_vertex_to_process = lambda: min(dict(filter(lambda item: item[0] not in processed, table.items())),
                         key=lambda key: table[key][0])
    vertex_to_process = calculate_vertex_to_process()
    print(vertex_to_process)

    while vertex_to_process != end_vertex:
        branches = {vertex: cost for vertex, cost in graph.get_branches_from(vertex_to_process).items() if
                    vertex not in processed}
        print(branches)
        for vertex, cost in branches.items():
            dist_from_start_vertex = table[vertex_to_process][0] + cost
            if dist_from_start_vertex < table[vertex][0]:
                table[vertex] = [dist_from_start_vertex, vertex_to_process]

        processed.append(vertex_to_process)
        vertex_to_process = calculate_vertex_to_process()

    return table





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
print(shortest_path(g, "A", "G"))





