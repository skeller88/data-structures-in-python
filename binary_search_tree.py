__author__ = 'Shane'


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __contains__(self, key):
        return bool(self.get(key))

    def __delitem__(self, key):
        self.delete(key)

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, val):
        self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __put_child_node(self, key, val, node):
        if key > node.key:
            if node.has_right_node():
                self.__put_child_node(key, val, node.right)
            else:
                self.size += 1
                node.right = TreeNode(key, val, node)
        elif key < node.key:
            if node.has_left_node():
                self.__put_child_node(key, val, node.left)
            else:
                self.size += 1
                node.left = TreeNode(key, val, node)
        else:
            node.val = val

    def __get_child_node(self, key, node):
        if not node:
            return None
        elif key == node.key:
            return node.val
        elif key > node.key:
            if node.has_right_node:
                self.__get_child_node(key, node.right)
            else:
                return None
        else:
            if node.has_left_node:
                self.__get_child_node(key, node.left)
            else:
                return None

    def __find_child_node_to_delete(self, key, node):
        if not node:
            raise KeyError('Node with key ' + key + ' not in tree.')
        elif key == node.key:
            self.__delete_child_node(node)
        elif key > node.key:
            if node.has_right_node:
                self.__find_child_node_to_delete(key, node.right)
            else:
                return None
        else:
            if node.has_left_node:
                self.__find_child_node_to_delete(key, node.left)
            else:
                return None

    def __delete_child_node(self, node):
        if node.is_leaf():
            if node.is_left_child:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.has_both_children():
            node_to_swap = node.find_successor()

            self.__swap_nodes(node, node_to_swap)

            # node_to_swap now has the key and val of the node that will be
            # deleted
            self.__delete_child_node(node_to_swap)
        elif not node.left:
            if node.is_left_child:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else:
            if node.is_left.child:
                node.parent.left = node.left
            else:
                node.parent.right = node.left

    def __swap_nodes(self, node1, node2):
        node1.key, node2.key = node2.key, node1.key
        node1.val, node2.val = node2.val, node1.val

    def put(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
            self.size += 1
        elif self.root.val == val:
            self.root.val = val
        else:
            self.__put_child_node(key, val, self.root)

    def get(self, key):
        if not self.root:
            return None
        elif self.root.key == key:
            return self.root.val
        else:
            return self.__get_child_node(key, self.root)

    def find_max_left_subtree(self, node):
        parent = node
        node = node['left']

        while True:
            if not node['right']:
                return node['value'], node, parent, 'right'
            else:
                parent = node
                node = node['right']

    def find(self, value):
        node = self.root

        while node:
            if value == node['value']:
                return True
            elif value > node['value']:
                node = node['right']
            else:
                node = node['left']

        return False

    def find_min(self):
        min_node = self.root
        child_node = self.root['left']

        while child_node:
            child_node = child_node['left']

        return min_node

    def find_max(self):
        max_node = self.root
        child_node = self.root['right']

        while child_node:
            child_node = child_node['right']

        return max_node


class TreeNode:
    def __init__(self, key, val, parent=None, left=None, right=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def has_left_node(self):
        return self.left

    def has_right_node(self):
        return self.right

    def has_any_children(self):
        return self.left or self.right

    def has_both_children(self):
        return self.left and self.right

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return self == self.parent.right

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.has_any_children()

    def find_successor(self):
        """Only should be invoked in the body of
        BinarySearchTree.__delete_child_node()"""
        return self.right.find_min_child()

    def find_min_child(self):
        node = self

        while node.has_left_node():
            node = node.left

        return node
