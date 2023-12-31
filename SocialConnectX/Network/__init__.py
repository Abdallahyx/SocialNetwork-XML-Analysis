"""
A class representing a network of users and their connections.

Methods:
- most_influential(graph): Returns the most influential users based on the number of followers.
- most_active(graph): Returns the most active users based on the number of connections.
- mutual_followers(graph, node1_id, node2_id): Returns the mutual followers between two users.
- suggest_followers(graph): Suggests users to follow based on the connections of the existing users.
- create_graph(tree): Creates a graph from an XML tree representing user data.
- show_graph(graph): Visualizes the graph using NetworkX and Matplotlib.
- post_search(graph, keyword): Searches for posts containing a specific keyword.
"""