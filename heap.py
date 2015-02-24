__author__ = 'Shane'

class Heap:
    """Implemented as max heap."""
    def __init__(self, items=None):
        """Args:
        items (list): used to build heap
        """
        self.__storage = items if items else []
        self.heapify(self.__storage)

    def __len__(self):
        return len(self.__storage)

    def __swap(self, a, b):
        self.__storage[a], self.__storage[b] = (self.__storage[b],
                                                self.__storage[a])

    def __sift_up(self, ind):
        parent = (ind - 1) >> 1 if ind % 2 != 0 else (ind - 2) >> 1

        while parent >= 0:
            if self.__storage[ind] > self.__storage[parent]:
                self.__swap(ind, parent)
            else:
                break

            ind = parent
            parent = (ind - 2) >> 1 if ind % 2 == 0 else (ind - 1) >> 1

    def __sift_down(self, root, end):
        heap = self.__storage
        max = root
        left = (root << 1) + 1
        right = (root + 1) << 1

        if left < end and heap[left] > heap[root]:
            self.__swap(left, root)
            max = left

        if right < end and heap[right] > heap[root]:
            self.__swap(right, root)
            max = right

        if max != root:
            self.__sift_down(max, end)

    def heapify(self, items=None):
        """Args:
        items (list): used to build heap
        """
        self.__storage = items if items else self.__storage
        end = len(self)

        for ind in xrange(end - 1, -1, -1):
            self.__sift_down(ind, end)

    def heap_sort(self, items=None):
        self.heapify(items)

        for ind in xrange(len(self) - 1, 0, -1):
            self.__swap(0, ind)
            self.__sift_down(0, ind)

        return self.__storage

    def is_empty(self):
        return bool(self.__storage)

    def insert(self, item):
        self.__storage.append(item)
        self.__sift_up(len(self.__storage) - 1)

    def peek(self):
        return self.__storage[0]

    def pull_max(self):
        max = self.__storage.pop(0)

        self.heapify()

        return max

h1 = Heap([5,1,2,3,6,57,-99])
h2 = Heap()

print h1.peek()
print h1.heap_sort()
h1.insert(88)
print h1.peek()
print h1.heap_sort()