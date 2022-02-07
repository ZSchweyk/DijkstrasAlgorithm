from NodeClass import Node


class Graph:
    def __init__(self, nodes: list[Node]):
        self.nodes = {node.name: node for node in nodes}

    def get_branches_from(self, node_name: str):
        """Get all the branches adjacent to a given node.name. This is slightly different than Node's get_branches
        because the branches attribute has node objects as its keys, whereas this method returns a dict with
        the names of those node objects as keys."""
        try:
            return {node_obj.name: cost for node_obj, cost in self.nodes[node_name].get_branches().items()}
        except KeyError:
            raise Exception(f"\"{node_name}\" DNE in the nodes, {self.nodes}, of this Graph object.")

    def get_vertices(self):
        """Get all the vertices in the graph."""
        return tuple(self.nodes.keys())

    def shortest_path(self, start_vertex, end_vertex):
        """Returns a tuple containing the shortest path and total cost
        between start_vertex and end_vertex of a given table. See GraphVisualization.jpg and the table below
        to format the table properly to create a Graph object out of it."""

        # Construct a dictionary, with the keys representing the vertices and the values representing a list
        # containing the shortest distance from start_vertex and the previous vertex.
        #
        # Vertex | Shortest Distance from start_vertex | Previous Vertex
        # A      | 0                                   |
        # B      | infinity                            | A
        # C      | infinity                            | A
        # ...
        table = {}
        for vertex in self.get_vertices():
            # Assume that every vertex is infinitely far away
            table.update({vertex: [0 if vertex == start_vertex else float("inf"), ""]})

        processed = []  # Create a list to store all future processed vertices
        # A function that calculates the next vertex to process. First, it filters out every vertex that has been processed,
        # and then grabs the vertex with the shortest distance from start_vertex.
        calculate_vertex_to_process = lambda: min(dict(filter(lambda item: item[0] not in processed, table.items())),
                                                  key=lambda key: table[key][0])
        # Store the result of the function above in vertex_to_process
        vertex_to_process = calculate_vertex_to_process()

        # Start looping until the destination vertex is about to be processed
        while vertex_to_process != end_vertex:
            # Grab all the branches and costs that vertex_to_process has, filtering out all the vertices that have been
            # processed.
            branches = {vertex: cost for vertex, cost in self.get_branches_from(vertex_to_process).items() if
                        vertex not in processed}

            # Loop through each vertex and cost in the branches, and update the table accordingly.
            for vertex, cost in branches.items():
                # Calculate the distance from start_vertex to vertex_to_process
                dist_from_start_vertex = table[vertex_to_process][0] + cost
                if dist_from_start_vertex < table[vertex][0]:
                    # If that calculated distance is < the distance that's already in the table, updated it so that that
                    # value is the shortest distance from start_vertex to vertex_to_process
                    table[vertex] = [dist_from_start_vertex, vertex_to_process]

            # Append vertex_to_process to processed, which was defined above.
            processed.append(vertex_to_process)
            # Recalculate the next vertex to process, and update vertex_to_process to equal that new vertex for the next
            # loop iteration.
            vertex_to_process = calculate_vertex_to_process()

        # Create a list that will hold the shortest path from start_vertex to end_vertex.
        path = []
        # Create a variable to store a changing vertex. Personally, I didn't want to change the value of end_vertex.
        looping_vertex = end_vertex
        # Append end_vertex to the path; the while loop below will fill in the rest.
        path.append(looping_vertex)
        # This while loop basically is exactly the same as repeated VLOOKUPs in Excel/Google Sheets.
        while looping_vertex != start_vertex:
            # Append the value obtained from looping_vertex serving as the key to the table dictionary.
            path.append(table[looping_vertex][1])
            # Update the value of looping_vertex.
            looping_vertex = table[looping_vertex][1]

        # Return a tuple of the reversed version of path and the total cost of that shortest path.
        return path[::-1], table[end_vertex][0]
