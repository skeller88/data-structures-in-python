__author__ = 'Shane'
import linked_list


class HashTable:
    def __init__(self, size=10):
        self.__size = 10
        self.__storage = [None for n in xrange(self.__size)]

    def __hasher(self, item, size):
        h = 0

        highorder = h & 0xf8000000

        h = h << 5
        h = h ^ (highorder >> 27)

        for char in item:
            h = h ^ ord(char)

        return h % size

    def __setitem__(self, key, value):
        hash = self.__hasher(key, self.__size)
        bucket = self.__storage[hash]

        if not bucket:
            bucket = self.__storage[hash] = linked_list.LinkedList()

        if key in bucket:
            bucket.update_node(key, value)
        else:
            bucket.add_to_tail(key, value)

    def __getitem__(self, key):
        hash = self.__hasher(key, self.__size)
        bucket = self.__storage[hash]

        if not bucket:
            return None
        else:
            return bucket.get_node_value(key)

    def __delitem__(self, key):
        hash = self.__hasher(key, self.__size)
        bucket = self.__storage[hash]

        if bucket:
            bucket.remove_node(key)
