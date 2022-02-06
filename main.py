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
    table = {}
    for vertex in graph.get_vertices():
        table.update({vertex: [0 if vertex == start else float("inf"), ""]})
    print(table)
    processed = []
    vertex_to_process = min(dict(filter(lambda item: item[0] not in processed, table.items())),
                         key=lambda key: table[key][0])
    print(vertex_to_process)
    # table = {}
    # for row, vertex in enumerate(graph.get_vertices()):
    #     table.update({row: [vertex, 0 if vertex == start else float("inf"), ""]})
    # print(table)
    # processed = []
    # # Find the row to process
    # row_to_process = min(dict(filter(lambda item: item[1][0] not in processed, table.items())), key=lambda key: table[key][1])
    # print(row_to_process)
    #
    # while table[row_to_process][0] != finish:
    #     branches = {vertex: cost for vertex, cost in graph.get_branches_from(table[row_to_process][0]).items() if vertex not in processed}
    #     print(branches)
    #     processed.append(table[row_to_process][0])
    #     row_to_process = min(dict(filter(lambda item: item[1][0] not in processed, table.items())),
    #                          key=lambda key: table[key][1])
    # print("Done")





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





