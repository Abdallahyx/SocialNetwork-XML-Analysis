import networkx as nx
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def create_graph(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    G = nx.DiGraph()

    for user in root.findall("user"):
        user_id = int(user.find("id").text)

        if user.find("name") is not None:
            user_name = user.find("name").text
        else:
            user_name = "unknown"
        G.add_node(user_id, name=user_name)

        followers = user.find("followers")
        if followers is not None:
            for follower in followers.findall("follower"):
                follower_id = int(follower.find("id").text)
                G.add_edge(user_id, follower_id)

        user_posts = user.find("posts")
        if user_posts is not None:
            posts = []
            for post in user_posts.findall("post"):
                posts.append(post)

            G.nodes[user_id]['posts'] = posts

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8,
            font_color="black", font_weight="bold", edge_color="skyblue", arrowsize=10, connectionstyle="arc3,rad=0.1",
            edgecolors="#00b4d8")
    plt.show()

    return G
