# 1. Most Influential Users (Most Followers)
def most_influential(graph):
    user_ids = []
    out_degrees = []

    for user_id in graph.nodes:
        user_ids.append(user_id)
        out_degrees.append(len(list(graph.successors(user_id))))

    max_out_degree = max(out_degrees)

    most_influential_users = [user_ids[i] for i, degree in enumerate(out_degrees) if degree == max_out_degree]

    print(f"The most influential users are: {most_influential_users}")
    return most_influential_users


# 2. Most Active User (Connected to Lots of Users)
def most_active(graph):
    user_ids = []
    total_edges = []

    for user_id in graph.nodes:
        user_ids.append(user_id)
        total_edges.append(graph.degree(user_id))

    max_total_edges = max(total_edges)

    most_active_users = [user_ids[i] for i, degree in enumerate(total_edges) if degree == max_total_edges]

    print(f"The most active users are: {most_active_users}")
    return most_active_users


# 3.  Mutual followers between 2 users
def mutual_followers(graph, node1, node2):
    if node1 not in graph.nodes or node2 not in graph.nodes:
        print("Invalid nodes. Please provide existing nodes.")
        return None

    followers_node1 = []
    for successor in graph.successors(node1):
        followers_node1.append(successor)

    followers_node2 = []
    for successor in graph.successors(node2):
        followers_node2.append(successor)

    mut_followers = [follower for follower in followers_node1 if follower in followers_node2]
    print(f"Mutual followers between nodes {node1} and {node2}: {mut_followers}")
    return mut_followers


# 4.  Suggest users to follow
def suggest_followers(graph):
    suggested_followers = []

    for user in graph.nodes:
        user_suggestions = []

        for successor in graph.successors(user):
            for suggested_follower in graph.successors(successor):
                if suggested_follower not in graph.predecessors(user) and suggested_follower != user and suggested_follower not in user_suggestions:
                    user_suggestions.append(suggested_follower)

        suggested_followers.append((user, user_suggestions))

    for user, user_suggestions in suggested_followers:
        print(f"Suggested followers for User {user}: {user_suggestions}")

    return suggested_followers
