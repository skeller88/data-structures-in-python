__author__ = 'Shane'


from collections import defaultdict


class AdjacencyList:
    def __init__(self):
        self.__vertices = defaultdict(lambda: defaultdict(int))

    def add_vertex(self, val, neighbors=[]):
        for n in neighbors:
            n_val = n['value']
            self.__vertices[val][n_val] = n['weight']
            self.__vertices[n_val][val] = n['weight']

    def remove_vertex(self, val):
        del self.__vertices[val]

        for v in self.__vertices:
            del self.__vertices[v][val]

    def add_edge(self, v1, v2, w=1):
        self.__vertices[v1][v2] = w
        self.__vertices[v2][v1] = w

    def get_edge(self, v1, v2):
        return self.__vertices[v1][v2]

    def remove_edge(self, v1, v2):
        del self.__vertices[v1][v2]
        del self.__vertices[v2][v1]

    def bread_first_search(self, val):
        results = []
        visited = {}
        distance = 0
        vertices_to_traverse = [{'distance': distance, 'value': val}]

        while vertices_to_traverse:
            vertex = vertices_to_traverse.pop(0)
            value = vertex['value']

            results.append(vertex)

            neighbors = self.__vertices[value]
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

            for k in self.__vertices[vertex]:
                if k not in visited:
                    traverse(k, distance + 1)

        traverse(val)

        return results
