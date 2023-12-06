import networkx as nx
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def create_graph(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    G = nx.DiGraph()

    for user in root.findall(".//user"):
        user_id = int(user.find("id").text)
        G.add_node(user_id)

        followers = user.find("followers")
        if followers is not None:
            for follower in followers.findall("follower"):
                follower_id = int(follower.find("id").text)
                G.add_edge(user_id, follower_id)

        posts = user.find("posts")
        if posts is not None:
            post_texts = [post.text.strip() for post in posts.findall("post")]
            G.nodes[user_id]['posts'] = post_texts

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8,
            font_color="black", font_weight="bold", edge_color="skyblue", arrowsize=10, connectionstyle="arc3,rad=0.1",
            edgecolors="#00b4d8")
    plt.show()

    return G
