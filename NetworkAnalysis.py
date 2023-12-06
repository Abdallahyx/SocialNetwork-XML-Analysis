# 1. Most Influential Users (Most Followers)
def most_influential(graph):
    out_degrees = dict(graph.out_degree())
    max_out_degree = max(out_degrees.values())
    most_influential_users = [user for user, out_degree in out_degrees.items() if out_degree == max_out_degree]

    print(f"The most influential users are: {most_influential_users}")
    return


# 2. Most Active User (Connected to Lots of Users)
def most_active(graph):
    total_edges = dict(graph.degree())
    max_total_edges = max(total_edges.values())
    most_active_users = [user for user, degree in total_edges.items() if degree == max_total_edges]

    print(f"The most active users are: {most_active_users}")
    return


# 3.  Mutual followers between 2 users
def mutual_followers(graph, node1, node2):
    if node1 not in graph or node2 not in graph:
        print("Invalid nodes. Please provide existing nodes.")
        return None

    followers_node1 = set(graph.successors(node1))
    followers_node2 = set(graph.successors(node2))

    mutual_followers = followers_node1.intersection(followers_node2)
    print(f"Mutual followers between nodes {node1} and {node2}: {mutual_followers}")
    return list(mutual_followers)


# 4.  Suggest users to follow
def suggest_followers(graph):
    suggested_followers_dict = {}

    for user in graph.nodes:
        followers_of_followers = set()

        for successor in graph.successors(user):
            followers_of_followers.update(graph.successors(successor))

        suggested_followers = followers_of_followers - set(graph.predecessors(user)) - {user}
        suggested_followers_dict[user] = list(suggested_followers)

    for user, suggested_followers in suggested_followers_dict.items():
        print(f"Suggested followers for User {user}: {suggested_followers}")

    return suggested_followers_dict
