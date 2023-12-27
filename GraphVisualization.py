import networkx as nx
import matplotlib.pyplot as plt

from Graph import DirectedGraph
from XMLParser import Parse


def create_graph(xml_file):
    tree = Parse(xml_file)
    root = tree.getroot()

    if root is not None:
        graph = DirectedGraph()

        for user in root.findall("user"):
            user_id = user.find("id").value

            if user.find("name") is not None:
                user_name = user.find("name").value
            else:
                user_name = "unknown"
            graph.add_node(user_id, name=user_name)

            followers = user.find("followers")
            if followers is not None:
                for follower in followers.findall("follower"):
                    follower_id = follower.find("id").value
                    graph.add_edge(user_id, follower_id)

            user_posts = user.find("posts")
            if user_posts is not None:
                posts = []
                for post in user_posts.findall("post"):
                    posts.append(post)

                graph.add_posts(user_id, posts)

        # Create a directed graph from your data using NetworkX
        nx_graph = nx.DiGraph()

        for node in graph.nodes:
            nx_graph.add_node(node.id, name=node.name)
            for successor in node.successors:
                nx_graph.add_edge(node.id, successor.id)

        # Visualize the graph
        pos = nx.spring_layout(nx_graph)  # You can use different layout algorithms
        nx.draw(nx_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', arrowsize=10, font_size=8, edge_color="skyblue", connectionstyle="arc3,rad=0.1")
        plt.show()

        return graph
    else:
        print("Error: Tree root is not properly set.")
        return None