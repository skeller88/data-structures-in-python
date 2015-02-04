__author__ = 'Shane'
import linked_list


class HashTable:
    def __init__(self, size=10):
        self.__size = 4
        self.__size_used = 0
        self.__storage = [None for n in xrange(self.__size)]

    def __hasher(self, item, size):
        h = 0

        highorder = h & 0xf8000000

        h = h << 5
        h = h ^ (highorder >> 27)

        for char in item:
            h = h ^ ord(char)

        return h % size

    def __resize(self):
        old_storage = self.__storage

        self.__storage = [None for n in xrange(self.__size)]

        for bucket in old_storage:
            if bucket:
                node = bucket.remove_from_tail()

                while node:
                    key = node[0]
                    value = node[1]
                    self[key] = value
                    node = bucket.remove_from_tail()

    def __setitem__(self, key, value):
        hash = self.__hasher(key, self.__size)
        bucket = self.__storage[hash]

        if not bucket:
            self.__size_used += 1
            bucket = self.__storage[hash] = linked_list.LinkedList()

        if key in bucket:
            bucket.update_node(key, value)
        else:
            bucket.add_to_tail(key, value)

        if (self.__size_used/self.__size) >= 0.75:
            self.__size *= 2
            self.__resize()

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
        if not bucket.head:
            self.__size_used -= 1

            if (self.__size_used/self.__size) <= 0.25:
                self.__size *= 0.5
                self.__resize()
