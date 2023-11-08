from collections import deque

def build_graph(matrix):
    graph = {}
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                neighbors = []
                if i > 0 and matrix[i - 1][j] == 1:
                    neighbors.append((i - 1, j))
                if j > 0 and matrix[i][j - 1] == 1:
                    neighbors.append((i, j - 1))
                if i < rows - 1 and matrix[i + 1][j] == 1:
                    neighbors.append((i + 1, j))
                if j < cols - 1 and matrix[i][j + 1] == 1:
                    neighbors.append((i, j + 1))
                graph[(i, j)] = neighbors

    return graph

def find_shortest_path(matrix, start, end):
    graph = build_graph(matrix)
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        (x, y), steps = queue.popleft()
        visited.add((x, y))

        if (x, y) == end:
            return steps

        for neighbor in graph.get((x, y), []):
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))

    return -1

with open("input.txt", "r") as file:
    start_str, end_str, matrix_size_str, *matrix_str = file.read().splitlines()

start_x, start_y = map(int, start_str.split(", "))
end_x, end_y = map(int, end_str.split(", "))
rows, cols = map(int, matrix_size_str.split(", "))

matrix = []
for row in matrix_str:
    matrix.append([int(cell) for cell in row.split()])

shortest_path = find_shortest_path(matrix, (start_x, start_y), (end_x, end_y))

with open("output.txt", "w") as file:
    file.write(str(shortest_path))
