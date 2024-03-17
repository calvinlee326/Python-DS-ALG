class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # empty list to store a collection of TreeNode
        self.parent = None  # a node can only have one parent, clear define no parent assigned to it

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = '  ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        result = prefix + self.data + '\n'
        if self.children:
            for child in self.children:
                result += child.print_tree()
        return result


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    print(root.print_tree())
