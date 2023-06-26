class UndirectedGraph:
    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex not in self.graph:
            self.graph[start_vertex] = []
        self.graph[start_vertex].append(end_vertex)

        if end_vertex not in self.graph:
            self.graph[end_vertex] = []
        self.graph[end_vertex].append(start_vertex)

    def traverse_breadth_first(self, root):
        visited = []
        queue = [root]

        while len(queue) != 0:
            element = queue.pop(0)
            visited.append(element)

            for node in self.graph[element]:
                if node not in visited:
                    queue.append(node)

    def traverse_depth_first(self, root):
        return self._depth_first(root, [])

    def _depth_first(self, node, visited):
        visited.append(node)

        for neighbour in self.graph[node]:
            if neighbour not in visited:
                visited = self._depth_first(neighbour, visited)

        return visited

    def print(self):
        for key in self.graph:
            print(key, "=>", self.graph[key])
