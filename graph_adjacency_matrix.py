__author__ = 'Shane'


class AdjacencyMatrix:
    def __init__(self, size=8):
        self._matrix = [[0] * (size + 1) for n in xrange(size + 1)]

    def __len__(self):
        return len(self._matrix)

    def __contains__(self, item):
        if self._matrix.get(item):
            return True
        else:
            return False

    def add_edge(self, v1, v2, w):
        self._matrix[v1][v2] = w
        self._matrix[v2][v1] = w

    def get_edge(self, v1, v2):
        return self._matrix[v1][v2]

    def remove_edge(self, v1, v2):
        self._matrix[v1][v2] = 0
        self._matrix[v2][v1] = 0
