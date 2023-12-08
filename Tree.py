class Node:
    def __init__(self, key="", value=""):
        self.key = key
        self.value = value
        self.children = []

    def set_value(self, value):
        self.value = value

    def set_key(self, key):
        self.key = key

    def find(self, key):
        if self.key == key:
            return self

        for child in self.children:
            result = child.find(key)
            if result:
                return result

        return None


class Tree:
    def __init__(self):
        self.m_root = None

    def set_root(self, t):
        self.m_root = t

    def add_node(self, node, parent=None):
        if parent is None:
            parent = self.m_root
        parent.children.append(node)

    def getroot(self):
        return self.m_root

    def PrettifyFormat(self, depth=0, parent=None):
        if parent is None:
            parent = self.m_root
            depth = 0

        output = ""
        indentation = "    " * depth

        output += indentation + "<" + parent.key + f">{parent.value.lstrip()}\n"

        for i in range(len(parent.children)):
            node = parent.children[i]

            if node.children:
                output += self.PrettifyFormat(depth + 1, node)
            else:
                output += (
                    indentation
                    + "    <"
                    + node.key
                    + ">"
                    + node.value
                    + "</"
                    + node.key
                    + ">\n"
                )

        output += indentation + "</" + parent.key + ">\n"

        return output

    def MinifyFormat(self, parent=None):
        if parent is None:
            parent = self.m_root

        output = ""
        parent_value = parent.value.lstrip().rstrip()
        output += "<" + parent.key + f">{parent_value}"

        for i in range(len(parent.children)):
            node = parent.children[i]

            if node.children:
                output += self.MinifyFormat(node)
            else:
                output += (
                    "<"
                    + node.key
                    + ">"
                    + node.value.lstrip().rstrip()
                    + "</"
                    + node.key
                    + ">"
                )

        output += "</" + parent.key + ">"

        return output

    def findall(self, key, parent=None):
        if parent is None:
            parent = self.m_root

        result = []
        if parent.key == key:
            result.append(parent)

        for child in parent.children:
            result.extend(self.findall(key, child))

        return result


# # Example usage:
# # Create nodes and tree
# root_node = Node()
# root_node.key = "root"

# child1 = Node()
# child1.key = "child1"
# child1.set_value("value1")

# child2 = Node()
# child2.key = "child2"
# child2.set_value("value2")

# grandchild1 = Node()
# grandchild1.key = "grandchild1"
# grandchild1.set_value("value")

# grandchild2 = Node()
# grandchild2.key = "grandchild1"
# grandchild2.set_value("value")

# grandchild3 = Node()
# grandchild3.key = "grandchild1"
# grandchild3.set_value("value")

# grandchild4 = Node()
# grandchild4.key = "grandchild1"
# grandchild4.set_value("value")


# tree = Tree()
# tree.set_root(root_node)
# tree.add_node(child1, root_node)
# tree.add_node(child2, root_node)
# tree.add_node(grandchild1, child1)
# tree.add_node(grandchild2, child1)
# tree.add_node(grandchild3, child2)
# tree.add_node(grandchild4, child2)


# # Output the formatted tree
# formatted_tree = tree.MinifyFormat()
# print(formatted_tree)
# formatted_tree = tree.PrettifyFormat()
# print(tree.toJson())
