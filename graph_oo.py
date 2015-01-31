__author__ = 'Shane'


class Graph:
    def __init__(self):
        self._edges = {}
        self._vertices = {}
        self._size = 0

    def __contains__(self, vertex):
        if self._vertices[vertex]:
            return True
        return False

    def for_each_vertex(self, func):
        new_edges = new_vertices = {}

        for v in self._vertices:
            new_vertex = func(v) or v
            new_vertices[new_vertex] = True
            new_edges[new_vertex] = {}

            for neighbor in self._edges[v]:
                new_neighbor = func(neighbor)
                new_edges[new_vertex][new_neighbor] = True
                new_edges[new_neighbor] = new_edges.get(new_neighbor, {})
                new_edges[new_neighbor][new_vertex] = True

        self._vertices = new_vertices
        self._edges = new_edges

    def add_vertex(self, val, target_edge=None):
        self._vertices[val] = True
        self._edges[val] = {}
        self._size += 1

        if target_edge:
            self.add_edge(val, target_edge)

    def __delitem__(self, vertext):
        if not self._vertices.get(vertext):
            raise Exception('Node does not exist in the graph.')

        self._size -= 1
        del self._vertices[vertext]

    def add_edge(self, v1, v2):
        if not (self._vertices.get(v1) and self._vertices.get(v2)):
            raise Exception('One of the nodes does not exist in the graph.')

        self._edges[v1][v2] = True
        self._edges[v2][v1] = True

    def remove_edge(self, v1, v2):
        if not (self._vertices.get(v1) and self._vertices.get(v2)):
            raise Exception('One of the nodes does not exist in the graph.')

        del self._edges[v1][v2]
        del self._edges[v2][v1]
