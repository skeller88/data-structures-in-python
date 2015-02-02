__author__ = 'Shane'


from collections import defaultdict


class AdjacencyList:
    def __init__(self):
        self._vertices = defaultdict(lambda: defaultdict(int))

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

    def bread_first_search(self, val):
        results = []
        visited = {}
        distance = 0
        vertices_to_traverse = [{'distance': distance, 'value': val}]

        while vertices_to_traverse:
            vertex = vertices_to_traverse.pop(0)
            value = vertex['value']

            results.append(vertex)

            neighbors = self._vertices[value]
            distance += 1

            for k, v in neighbors.iteritems():
                if k not in visited:
                    vertices_to_traverse.append({
                        'distance': distance,
                        'value': k,
                        })

            visited[value] = True

        return results

    def depth_first_search(self, val):
        results = []
        visited = {}

        def traverse(vertex, distance=0):
            visited[vertex] = True

            results.append({
                'distance': distance,
                'value': vertex
            })

            for k in self._vertices[vertex]:
                if k not in visited:
                    traverse(k, distance + 1)

        traverse(val)

        return results
