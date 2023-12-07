class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.vertices.add(vertex1)
        self.vertices.add(vertex2)
        self.edges[vertex1].append(vertex2)

    def get_neighbors(self, vertex):
        return self.edges[vertex]

def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(vertex):
        if vertex in visited:
            return
        visited.add(vertex)
        for neighbor in graph.get_neighbors(vertex):
            dfs(neighbor)
        stack.append(vertex)

    for vertex in graph.vertices:
        dfs(vertex)

    return stack[::-1]
    # return stack

def main():

    input_file_path = "src/govern.in"
    output_file_path = "src/govern.out"

    with open(input_file_path, "r") as f:
        data = f.readlines()

    graph = Graph()
    for line in data:
        first_word, second_word = line.strip().split()
        graph.add_vertex(first_word)
        graph.add_vertex(second_word)
        graph.add_edge(first_word, second_word)

    sorted_vertices = topological_sort_dfs(graph)
    sorted_vertices.reverse()

    with open(output_file_path, "w") as f:
        for vertex in sorted_vertices:
            f.write(vertex + "\n")

if __name__ == "__main__":
    main()
