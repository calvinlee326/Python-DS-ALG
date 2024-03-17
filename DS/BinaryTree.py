'''
Binary Search Tree (BST), Every node has at most 2 child nodes
at left lower than parent, at right greater than parent, element not duplicated

Every iteration we reduce search space by 1/2
n = 8, 8-4-2-1 -> 3 iterations
Search Complexity = O(log n)
'''


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # value might be left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # value might be right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False




def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [7, 22, 4, 62, 11, 3, 8, 66]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(62))
