__author__ = 'Shane'


from collections import defaultdict


class AdjacencyList:
    def __init__(self):
        self._vertices = defaultdict(lambda: defaultdict(dict))

    def add_vertex(self, val, neighbors=[]):
        for n in neighbors:
            n_val = n['value']
            self._vertices[val][n_val] = n['weight']
            self._vertices[n_val][val] = n['weight']

    def remove_vertex(self, val):
        del self._vertices[val]

        for v in self._vertices:
            del self._vertices[v][val]

    def add_edge(self, v1, v2, w=1):
        self._vertices[v1][v2] = w
        self._vertices[v2][v1] = w

    def get_edge(self, v1, v2):
        return self._vertices[v1][v2]

    def remove_edge(self, v1, v2):
        del self._vertices[v1][v2]
        del self._vertices[v2][v1]
