__author__ = 'Shane'


class Graph:
    def __init__(self):
        self._edges = {}
        self._vertices = {}
        self._size = 0

    def __contains__(self, item):
        if self._vertices[item]:
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

    def add_node(self, val, target_edge=None):
        self._vertices[val] = True
        self._edges[val] = {}
        self._size += 1

        if target_edge:
            self.add_edge(val, target_edge)

    def __delitem__(self, key):
        if not self._vertices.get(key):
            raise Exception('Node does not exist in the graph.')

        self._size -= 1
        del self._vertices[key]

    def add_edge(self, node_1, node_2):
        if not (self._vertices.get(node_1) and self._vertices.get(node_2)):
            raise Exception('One of the nodes does not exist in the graph.')

        self._edges[node_1][node_2] = True
        self._edges[node_2][node_1] = True

    def remove_edge(self, node_1, node_2):
        if not (self._vertices.get(node_1) and self._vertices.get(node_2)):
            raise Exception('One of the nodes does not exist in the graph.')

        del self._edges[node_1][node_2]
        del self._edges[node_2][node_1]
