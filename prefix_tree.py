__author__ = 'Shane'


class PrefixTree:
    def __init__(self):
        self.root = {
            'children': {},
            'value': ""
        }

    def __contains__(self, word):
        current_node = self.root
        prefix = ""

        for char in word:
            prefix += char
            if current_node['children'].get(char):
                current_node = current_node['children'][char]
            else:
                return False

        return True

    def add(self, word):
        current_node = self.root
        prefix = ""

        # for each char in the word
        for char in word:
            prefix += char
            if current_node['children'].get(char):
                current_node = current_node['children'][char]
            else:
                current_node['children'][char] = self._make_node(prefix)
                current_node = current_node['children'][char]

    def __delitem__(self, word):
        current_node = self.root
        prefix = ""

        for i, char in enumerate(word):
            prefix += char
            if current_node['children'].get(char):
                if i == len(word) - 1:
                    del current_node['children'][char]
                else:
                    current_node = current_node['children'][char]
            else:
                msg = 'No match at prefix {0}'.format(prefix)
                raise Exception(msg)

        del current_node

    def _make_node(self, prefix):
        return {
            'children': {},
            'value': prefix
        }
