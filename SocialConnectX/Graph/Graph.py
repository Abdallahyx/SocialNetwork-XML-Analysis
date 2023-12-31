class Node:
    def __init__(self, node_id, name, posts=None):
        """
        Initialize a Node object with the given node_id, name, and optional posts.
        """
        self.id = node_id
        self.name = name
        self.posts = posts if posts is not None else []  # Initialize posts as an empty list if not provided
        self.successors = []  # List to store the successor nodes
        self.predecessors = []  # List to store the predecessor nodes

    def set_id(self, id):
        """
        Set the node_id of the Node object.
        """
        self.id = id

    def set_name(self, name):
        """
        Set the name of the Node object.
        """
        self.name = name

    def set_posts(self, posts):
        """
        Set the posts of the Node object.
        """
        self.posts = posts


class DirectedGraph:
    def __init__(self):
        """
        Initialize a DirectedGraph object with an empty list of nodes.
        """
        self.nodes = []

    def find_node(self, user_id):
        """
        Find and return the Node object with the given user_id.
        If no such node exists, return None.
        """
        for node in self.nodes:
            if node.id == user_id:
                return node
        return None

    def add_node(self, user_id, name):
        """
        Add a new Node object with the given user_id and name to the graph if it doesn't already exist.
        """
        if not self.find_node(user_id):
            self.nodes.append(Node(user_id, name))

    def add_edge(self, user_id, follower_id, follower_name):
        """
        Add an edge between the Node object with user_id and the Node object with follower_id.
        If any of the nodes don't exist, create them before adding the edge.
        """
        user_node = self.find_node(user_id)
        follower_node = self.find_node(follower_id)

        if not follower_node:
            follower_node = Node(follower_id, follower_name)
            self.nodes.append(follower_node)

        if user_node and follower_node:
            user_node.successors.append(follower_node)
            follower_node.predecessors.append(user_node)

    def add_posts(self, user_id, posts):
        """
        Set the posts of the Node object with the given user_id.
        """
        node = self.find_node(user_id)
        if node:
            node.set_posts(posts)

    def successors(self, user_id):
        """
        Return a list of successor nodes for the Node object with the given user_id.
        If the node doesn't exist, return an empty list.
        """
        node = self.find_node(user_id)
        return node.successors if node else []

    def predecessors(self, user_id):
        """
        Return a list of predecessor nodes for the Node object with the given user_id.
        If the node doesn't exist, return an empty list.
        """
        node = self.find_node(user_id)
        return node.predecessors if node else []

    def degree(self, user_id):
        """
        Return the degree of the Node object with the given user_id.
        The degree is the sum of the number of successors and predecessors.
        If the node doesn't exist, return 0.
        """
        node = self.find_node(user_id)
        return len(node.successors) + len(node.predecessors) if node else 0
