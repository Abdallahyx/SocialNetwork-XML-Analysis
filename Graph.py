class Node:
    def __init__(self, node_id, name, posts=None):
        self.id = node_id
        self.name = name
        self.posts = posts if posts is not None else []
        self.successors = []
        self.predecessors = []

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_posts(self, posts):
        self.posts = posts


class DirectedGraph:
    def __init__(self):
        self.nodes = []

    def find_node(self, user_id):
        for node in self.nodes:
            if node.id == user_id:
                return node
        return None

    def add_node(self, user_id, name):
        if not self.find_node(user_id):
            self.nodes.append(Node(user_id, name))

    def add_edge(self, user_id, follower_id, follower_name):
        user_node = self.find_node(user_id)
        follower_node = self.find_node(follower_id)

        if not follower_node:
            follower_node = Node(follower_id, follower_name)
            self.nodes.append(follower_node)

        if user_node and follower_node:
            user_node.successors.append(follower_node)
            follower_node.predecessors.append(user_node)

    def add_posts(self, user_id, posts):
        node = self.find_node(user_id)
        if node:
            node.set_posts(posts)

    def successors(self, user_id):
        node = self.find_node(user_id)
        return node.successors if node else []

    def predecessors(self, user_id):
        node = self.find_node(user_id)
        return node.predecessors if node else []

    def degree(self, user_id):
        node = self.find_node(user_id)
        return len(node.successors) + len(node.predecessors) if node else 0


# Example Usage:
# graph = DirectedGraph()
#
# graph.add_node(1, "User1")
# graph.add_node(2, "User2")
# graph.add_edge(1, 2)
# graph.add_posts(1, ["Post1", "Post2"])
#
# print([node.id for node in graph.successors(1)])
# print([node.id for node in graph.predecessors(2)])
# print(graph.degree(1))
