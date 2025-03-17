class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

    def is_leaf(self):
        return len(self.children) == 0

    def is_full(self):
        return len(self.keys) == 2

    def insert_into_node(self, key):
        self.keys.append(key)
        self.keys.sort()

    def split(self):
        middle_key = self.keys[1]
        left_child = Node(keys=[self.keys[0]], children=self.children[:2])
        right_child = Node(keys=[self.keys[2]], children=self.children[2:])
        return middle_key, left_child, right_child


class TwoThreeTree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        if self.root.is_full():
            middle_key, left_child, right_child = self.root.split()
            new_root = Node(keys=[middle_key], children=[left_child, right_child])
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.is_leaf():
            node.insert_into_node(key)
        else:
            if key < node.keys[0]:
                child_index = 0
            elif len(node.keys) == 1 or key < node.keys[1]:
                child_index = 1
            else:
                child_index = 2

            child = node.children[child_index]
            if child.is_full():
                middle_key, left_child, right_child = child.split()
                node.keys.insert(child_index, middle_key)
                node.children[child_index] = left_child
                node.children.insert(child_index + 1, right_child)

                if key < node.keys[child_index]:
                    child = left_child
                else:
                    child = right_child

            self._insert_non_full(child, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if key in node.keys:
            return True
        elif node.is_leaf():
            return False
        else:
            if key < node.keys[0]:
                return self._search(node.children[0], key)
            elif len(node.keys) == 1 or key < node.keys[1]:
                return self._search(node.children[1], key)
            else:
                return self._search(node.children[2], key)


# Example usage:
tree = TwoThreeTree()
keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]

for key in keys_to_insert:
    tree.insert(key)

print(tree.search(10))  # Output: True
print(tree.search(15))  # Output: False