"""
Represents a directed graph.

Attributes:
    nodes (list): A list of nodes in the graph.

Methods:
    find_node(user_id): Finds a node with the given user ID.
    add_node(user_id, name): Adds a new node to the graph.
    add_edge(user_id, follower_id, follower_name): Adds an edge between two nodes in the graph.
    add_posts(user_id, posts): Sets the posts for a node in the graph.
    successors(user_id): Returns the successors of a node in the graph.
    predecessors(user_id): Returns the predecessors of a node in the graph.
    degree(user_id): Returns the degree of a node in the graph.
"""